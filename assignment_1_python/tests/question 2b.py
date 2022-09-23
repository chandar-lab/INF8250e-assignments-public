test = {   'name': 'question 2b',
    'points': [5, 10],
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> dummy_env=FrozenLakeEnv(map_name="2x2", slip_rate=0)\n'
                                               '>>> dummy_pi = np.array([[0, 0, 1, 0],[0,1,0,0],[0,0,1,0],[0,1,0,0]])\n'
                                               '>>> dummy_v = policy_evaluation(dummy_env, dummy_pi)\n'
                                               '>>> np.testing.assert_allclose(dummy_v,[-1.99, -1, -100, 0])\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> dummy_env=FrozenLakeEnv(map_name="2x2", slip_rate=0)\n'
                                               '>>> dummy_v = np.zeros(dummy_env.nS)\n'
                                               '>>> dummy_pi = np.random.rand(dummy_env.nS,dummy_env.nA)\n'
                                               '>>> \n'
                                               '>>> dummy_pi = dummy_pi/dummy_pi.sum(axis=1,keepdims=True)\n'
                                               '>>> \n'
                                               '>>> for iter in range(100):\n'
                                               '...   dummy_v = policy_evaluation(dummy_env,dummy_pi,1e-8)\n'
                                               '...   dummy_pi, dummy_policy_stable = policy_improvement(dummy_env,dummy_v,dummy_pi)\n'
                                               '>>> \n'
                                               '>>> np.testing.assert_allclose(dummy_pi[:2, :],np.array([[0, 0, 1, 0], [0, 1, 0, 0]]))\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
