import pickle


# imelda = ('more Mayhem', 
#             'IMelda May', 
#             '2011', 
#             ((1, 'Pulling the rug'), 
#              (2, 'Psycho'), 
#              (3, 'Mayhem'), 
#              (4, 'Kentish Town Waltz')
#             )
#         )
        

# with open("imelda.pickle",  "wb") as pickle_file:
#     pickle.dump(imelda, pickle_file)

with open("imelda.pickle",  "rb") as pickle_file:
   imelda2 =  pickle.load(pickle_file)

print(imelda2)