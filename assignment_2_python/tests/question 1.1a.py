test = {   'name': 'question 1.1a',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> dummy_states = [0, 5, 0, 0, 0, 0, 5, 0, 5, 0, 0, 0, 5, 0, 0, 5, 5, 6, 11, 11]\n'
                                               '>>> dummy_actions = [1, 3, 0, 0, 3, 1, 3, 1, 3, 0, 0, 1, 0, 3, 1, 0, 2, 1, 2]\n'
                                               '>>> dummy_rewards = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -100]\n'
                                               '>>> \n'
                                               '>>> true_answer = {(0, 1): -51.777145476657445,\n'
                                               '...  (5, 3): -53.44962681753415,\n'
                                               '...  (0, 0): -55.21013349214122,\n'
                                               '...  (0, 3): -59.013998329242355,\n'
                                               '...  (5, 0): -78.80735124999998,\n'
                                               '...  (5, 2): -92.2,\n'
                                               '...  (6, 1): -96.0,\n'
                                               '...  (11, 2): -100.0}\n'
                                               '...                                                        \n'
                                               '>>> visited_states_returns = fv_mc_estimation(dummy_states, dummy_actions, dummy_rewards, discount=0.95)\n'
                                               '>>> for sa in true_answer:\n'
                                               '...     assert sa in visited_states_returns\n'
                                               '...     np.testing.assert_allclose(true_answer[sa], visited_states_returns[sa])\n'
                                               '>>> assert len(true_answer) == len(visited_states_returns)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
