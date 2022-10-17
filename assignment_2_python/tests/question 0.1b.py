OK_FORMAT = True

test = {   'name': 'question 0.1b',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> true_states = np.zeros(52)\n'
                                               '>>> true_actions = np.ones(51) *3\n'
                                               '>>> true_rewards =  np.ones(51)* -1\n'
                                               '>>> true_rewards[-1] = -100\n'
                                               '>>> \n'
                                               '>>> env = FrozenLakeEnv(map_name="2x2", slip_rate=0)\n'
                                               '>>> dummy_state_action_values = np.arange(16*4).reshape(16,4)\n'
                                               '>>> dummy_pi = make_eps_greedy_policy(dummy_state_action_values, 0.)\n'
                                               '>>> states, actions, rewards = generate_episode(dummy_pi, env)\n'
                                               '>>> \n'
                                               '>>> np.testing.assert_allclose(len(states), 52)\n'
                                               '>>> np.testing.assert_allclose(states, true_states)\n'
                                               '>>> np.testing.assert_allclose(actions, true_actions)\n'
                                               '>>> np.testing.assert_allclose(rewards, true_rewards)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
