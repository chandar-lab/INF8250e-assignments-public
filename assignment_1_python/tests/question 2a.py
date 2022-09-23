test = {   'name': 'question 2a',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> dummy_env = FrozenLakeEnv(map_name="2x2", slip_rate=0)\n'
                                               '>>> dummy_pi = np.array([[0, 0, 1, 0],[0,1,0,0],[0,0,1,0],[0,1,0,0]])\n'
                                               '>>> ret, steps = generate_episode(dummy_pi, dummy_env)\n'
                                               '>>> np.testing.assert_allclose(ret,-2)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
