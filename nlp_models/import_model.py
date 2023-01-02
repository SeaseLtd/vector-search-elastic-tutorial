import elasticsearch
from pathlib import Path
from eland.ml.pytorch import PyTorchModel
from eland.ml.pytorch.transformers import TransformerModel

# Elastic configuration.
ELASTIC_ADDRESS = "http://localhost:9200"
# Uncomment the following lines if start ES with SECURITY ENABLED.
#ELASTIC_ADDRESS = "https://localhost:9200"
#ELASTIC_PASSWORD = "<your-password>"
#CA_CERTS_PATH = "path/to/http_ca.crt"

def main():
        # Load a Hugging Face transformers model directly from the model hub
        tm = TransformerModel("sentence-transformers/all-MiniLM-L6-v2", "text_embedding")

        # Export the model in a TorchScript representation which Elasticsearch uses
        tmp_path = "models"
        Path(tmp_path).mkdir(parents=True, exist_ok=True)
        model_path, config, vocab_path = tm.save(tmp_path)

        # Import model into Elasticsearch
        client = elasticsearch.Elasticsearch(hosts=[ELASTIC_ADDRESS])
        # Use this instead, IF using SECURITY ENABLED.
        # client = Elasticsearch(hosts=[ELASTIC_ADDRESS], ca_certs=CA_CERTS_PATH, basic_auth=("elastic", ELASTIC_PASSWORD))

        ptm = PyTorchModel(client, tm.elasticsearch_model_id())
        ptm.import_model(model_path=model_path, config_path=None, vocab_path=vocab_path, config=config)


if __name__ == "__main__":
    main()