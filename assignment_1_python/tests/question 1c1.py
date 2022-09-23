test = {   'name': 'question 1c1',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> N=10\n'
                                               '>>> for n in range(N):\n'
                                               '...     dummy_bandit = Bandit(n_arm=3, n_pulls=1000, actual_ctr=[0, 1.0, 0])\n'
                                               '...     rew_rec_n, avg_ret_rec_n, tot_reg_rec_n = ucb(dummy_bandit, c=1)\n'
                                               '...     np.testing.assert_allclose(tot_reg_rec_n[-1],10, atol=2)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
