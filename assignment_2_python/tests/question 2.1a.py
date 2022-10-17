OK_FORMAT = True

test = {   'name': 'question 2.1a',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> # Some basic testing\n'
                                               '>>> dummy_states = [0, 5, 0, 0, 0, 0, 5, 0, 5, 0, 0, 0, 5, 0, 0, 5, 5]\n'
                                               '>>> dummy_actions = [1, 3, 0, 0, 3, 1, 3, 1, 3, 0, 0, 1, 0, 3, 1, 0]\n'
                                               '>>> dummy_rewards = [-1, -1, -1, -1, -1, -1, -1, -10, -1, -100, -1, -1, -1, -1, -1, -1]\n'
                                               '>>> \n'
                                               '>>> predicted_answer = ev_mc_estimate(dummy_states, dummy_actions,\n'
                                               '...                                               dummy_rewards, discount=0.99)\n'
                                               '>>> \n'
                                               '>>> np.testing.assert_allclose(len(predicted_answer.keys()), 2) # Only two distinct states \n'
                                               '...                                                             #are visited in the dummy episode\n'
                                               '>>> np.testing.assert_allclose(len(predicted_answer[0]), 11) # State 0 is visited 11 ttimes\n'
                                               '>>> \n'
                                               '>>> # Make sure inner type is correct\n'
                                               '>>> for k in predicted_answer:\n'
                                               '...     assert type(predicted_answer[k]) == list\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> answer = {0: [-86.11741938069248,\n'
                                               '...   -87.86595182194927,\n'
                                               '...   -88.75348668883765,\n'
                                               '...   -89.64998655438147,\n'
                                               '...   -92.57574399432471,\n'
                                               '...   -93.44530557527264,\n'
                                               '...   -92.31232075836408,\n'
                                               '...   -93.24476844279201,\n'
                                               '...   -94.18663479069899,\n'
                                               '...   -96.09900499,\n'
                                               '...   -96.059601],\n'
                                               '...  5: [-86.98729230372979,\n'
                                               '...   -93.51085251951991,\n'
                                               '...   -94.38919755078044,\n'
                                               '...   -95.13801494009999,\n'
                                               '...   -97.0299,\n'
                                               '...   -98.00999999999999],\n'
                                               '...  6: [-99.0],\n'
                                               '...  11: [-100.0]}\n'
                                               '>>> \n'
                                               '>>> dummy_states = [0, 5, 0, 0, 0, 0, 5, 0, 5, 0, 0, 0, 5, 0, 0, 5, 5, 6, 11, 11]\n'
                                               '>>> dummy_actions = [1, 3, 0, 0, 3, 1, 3, 1, 3, 0, 0, 1, 0, 3, 1, 0, 2, 1, 2]\n'
                                               '>>> dummy_rewards = [0, 0, 0, 0, 2, 0, -1, 0, -3, 0, 0, 0, 0, -1, 0, 0, 0, 0, -100]\n'
                                               '>>> \n'
                                               '>>> predicted_answer = ev_mc_estimate(dummy_states, dummy_actions, dummy_rewards, 0.99)\n'
                                               '>>> \n'
                                               '>>> np.testing.assert_allclose(len(answer), len(predicted_answer))\n'
                                               '>>> for k in answer:\n'
                                               '...     np.testing.assert_allclose(answer[k], predicted_answer[k])\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
