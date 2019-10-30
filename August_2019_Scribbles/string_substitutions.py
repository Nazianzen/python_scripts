# form = '''\
#     Dear %(name)s,
#         Please return my %(item)s and pay the sum of $%(amount)0.2f.
#                                             Yours Sincerely,
#                                             Gideon
#         '''
# print(form % {
#     'name':'Mr Bush',
#     'item': 'Blender',
#     'amount': 50,
# })

form = '''\
    Dear {name},
        Please return my {item} and pay the sum of ${amt:0.2f}.
                                            Yours Sincerely,
                                            Gideon
'''
print(form.format(
    name = 'Mr Charles',
    item = 'freezer',
    amt = 50.00
))
