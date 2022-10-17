OK_FORMAT = True

test = {   'name': 'question 1.2a',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> for epsilon in [0, 0.01, 0.15, 0.9]:\n'
                                               '...     all_actions = []\n'
                                               '...     dummy_state_action_values = np.ones((16, 4))\n'
                                               '...     dummy_state_action_values[:, 1] = 10\n'
                                               '...     test_pi = make_eps_greedy_policy_distribution(dummy_state_action_values, epsilon)\n'
                                               '...     states = list(range(16))\n'
                                               '...     for s in states:\n'
                                               '...         action_dist = test_pi(s)\n'
                                               '...         np.testing.assert_allclose(action_dist[1], 1 - epsilon + epsilon/4)\n'
                                               '...         np.testing.assert_allclose(action_dist[0], epsilon/4)\n'
                                               '...         np.testing.assert_allclose(action_dist[2:], epsilon/4)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
