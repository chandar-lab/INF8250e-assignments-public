test = {   'name': 'question 1d2',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> dummy_bandit = Bandit(n_arm=3, n_pulls=1000, actual_ctr=[0, 1.0, 0])\n'
                                               '>>> N=10\n'
                                               '>>> for n in range(N):\n'
                                               '...     rew_rec_n, avg_ret_rec_n, tot_reg_rec_n = boltzmann(dummy_bandit, tau=1e8) # uniform sampling\n'
                                               '...     np.testing.assert_allclose(tot_reg_rec_n[-1],666.0, atol=50)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
