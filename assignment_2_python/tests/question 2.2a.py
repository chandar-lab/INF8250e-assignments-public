OK_FORMAT = True

test = {   'name': 'question 2.2a',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> answer = [ -1.49378919,  -2.96526431,  -4.41475871,  -5.84260071,\n'
                                               '...         -7.24911376,  -8.63461647,  -9.99942269, -11.34384158,\n'
                                               '...        -12.66817769, -13.97273101]\n'
                                               '>>> \n'
                                               '>>> env = FrozenLakeEnv(map_name="6x5", slip_rate=0.)\n'
                                               '>>> \n'
                                               '>>> dummy_state_action_values = np.arange(30*4).reshape(30,4)\n'
                                               '>>> dummy_pi = make_eps_greedy_policy(dummy_state_action_values, 0.)\n'
                                               '>>> \n'
                                               '>>> dummy_state_vals = td0(dummy_pi, env, step_size=0.01, num_episodes=10)\n'
                                               '>>> \n'
                                               '>>> np.testing.assert_allclose(np.array(answer), np.array(dummy_state_vals)[:, 0])\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
