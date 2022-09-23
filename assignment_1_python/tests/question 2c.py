test = {   'name': 'question 2c',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> dummy_env=FrozenLakeEnv(map_name="2x2", slip_rate=0)\n'
                                               '>>> \n'
                                               '>>> dummy_v = np.zeros(dummy_env.nS)\n'
                                               '>>> _, _, dummy_v, dummy_pi = value_iteration_with_performance(dummy_env)\n'
                                               '>>> np.testing.assert_allclose(dummy_v,[-1.99, -1, -100, 0])\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
