# interpreter test
#
from interpreter import interpreter

interpreter.llm.model = "gpt-4o-mini"
interpreter.auto_run = True
interpreter.chat("Plot AAPL and META's normalized stock prices")