from parlai.core.agents import Agent
from parlai.core.params import ParlaiParser
from parlai.core.worlds import create_task

parser = ParlaiParser(True, True)
parser.add_pytorch_datateacher_args()
parser.set_defaults(task="personachat")
parser.set_defaults(download_path=".")
parser.set_defaults(datapath=".")

parser.set_defaults(datatype="train")

opt = parser.parse_args()
agent = Agent(opt)
world = create_task(opt, agent)

parser.set_defaults(datatype="valid")

opt = parser.parse_args()
agent = Agent(opt)
world = create_task(opt, agent)

parser.set_defaults(datatype="test")

opt = parser.parse_args()
agent = Agent(opt)
world = create_task(opt, agent)

