test = {   'name': 'question 1a',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> def temp_call(dummy_bandit, arm):\n'
                                               '...     dummy_bandit.pull(arm)\n'
                                               '>>> \n'
                                               '>>> dummy_bandit = Bandit(n_arm=3, actual_ctr=[0.0, 1, 0.0])\n'
                                               '>>> test_arms = [0, 2, 1, 0, 0, 0, 2]\n'
                                               '>>> for arm in test_arms:\n'
                                               '...     temp_call(dummy_bandit, arm)\n'
                                               '>>> np.testing.assert_allclose(dummy_bandit.impressions[0],4)\n'
                                               '>>> np.testing.assert_allclose(dummy_bandit.clicks[1],1)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
