test = {   'name': 'question 1b1',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> N=20\n'
                                               '>>> dummy_bandit = Bandit(n_arm=3, n_pulls=1000, actual_ctr=[1, 0.0, 0.0])\n'
                                               '>>> for n in range(N):\n'
                                               '...     rew_rec_n, avg_ret_rec_n, tot_reg_rec_n = eps_greedy(dummy_bandit, eps=1)\n'
                                               '...     np.testing.assert_allclose(tot_reg_rec_n[-1],660,atol=60)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
