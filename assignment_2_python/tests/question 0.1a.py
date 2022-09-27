OK_FORMAT = True

test = {   'name': 'question 0.1a',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> for epsilon in [0, 0.01, 0.15, 0.9]:\n'
                                               '...     dummy_state_action_values = np.ones((16, 4))\n'
                                               '...     dummy_state_action_values[:, 1] = 10\n'
                                               '...     test_pi = make_eps_greedy_policy(dummy_state_action_values, epsilon)\n'
                                               '...     states = list(range(16)) * 10000\n'
                                               '...     all_actions = []\n'
                                               '...     for s in states:\n'
                                               '...         action = test_pi(s)\n'
                                               '...         all_actions.append(action)\n'
                                               '...     expected_rate = (1-epsilon + epsilon/4)\n'
                                               '...     np.testing.assert_allclose(np.sum(np.array(all_actions) == 1)/len(states), expected_rate, atol=0.015)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
