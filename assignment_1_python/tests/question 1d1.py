test = {   'name': 'question 1d1',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> N=1000\n'
                                               '>>> dummy_x = [20, 100, 60]\n'
                                               '>>> tmp_sum = []\n'
                                               '>>> for n in range(N):\n'
                                               '...     dummy_idx = boltzmann_policy(dummy_x, tau=1e10) # uniform sampling\n'
                                               '...     tmp_sum.append(dummy_x[dummy_idx])\n'
                                               '>>> np.testing.assert_allclose(np.mean(tmp_sum), 60, atol=5)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
