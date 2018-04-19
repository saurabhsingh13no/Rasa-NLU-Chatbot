from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, config, model_dir):
    training_data = load_data(data)
    trainer = Trainer(RasaNLUConfig(config))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name="weathernlu")

def run_nlu():
    # load model
    interpreter = Interpreter.load("../models/nlu/default/weathernlu",
                                   RasaNLUConfig("../config_spacy.json"))

    # test on user input
    # print (interpreter.parse(u"I am planning my holiday to Boston . I wonder "
    #                          u"what is the weather out there."))

    print (interpreter.parse(u'what is the weather in Boston'))


if __name__ == "__main__":
    # train_nlu("../data/data.json","../config_spacy.json","../models/nlu")

    run_nlu()
