import time

import aiml

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")
# try:
#     while True:
#         input_text = input(">Human: ")
#         response = kernel.respond(input_text)
#         print(">Bot: " + response)
# except KeyboardInterrupt:
#     print('Interrupted by user')
while True:
    input_text = input(">Human: ")
    response = kernel.respond(input_text)
    print(">Bot: "+response)
    time.sleep(0.5)