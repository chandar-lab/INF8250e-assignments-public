OK_FORMAT = True

test = {   'name': 'question 2a.3',
    'points': [2, 2, 2, 3, 3],
    'suites': [   {   'cases': [   {   'code': '>>> test_len_rollout = 5\n'
                                               '>>> test_d = np.array([True for _ in range(test_len_rollout)])\n'
                                               '>>> test_r = np.ones(test_len_rollout)\n'
                                               '>>> assert_equal = functools.partial(torch.testing.assert_close, rtol=0, atol=0)\n'
                                               '>>> test_ret = discounted_returns(test_r, test_d, 0.99)\n'
                                               '>>> assert_equal(test_ret.shape[0], test_len_rollout)\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> assert_equal = functools.partial(torch.testing.assert_close, rtol=1e-5, atol=0)\n'
                                               '>>> test_rewards = [1.0,2.0,3.0,4.0,2.0,1.0]\n'
                                               '>>> test_dones = [False, False, True, False, False, True]\n'
                                               '>>> test_return = discounted_returns(test_rewards, test_dones, 0.5)\n'
                                               '>>> actual_return = np.array([2.75, 3.5, 3.0, 5.25, 2.5, 1.0])\n'
                                               '>>> assert_equal(test_return, actual_return)\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> assert_equal = functools.partial(torch.testing.assert_close, rtol=1e-5, atol=0)\n'
                                               '>>> test_rewards = [1.0,2.0,3.0,4.0,2.0,1.0]\n'
                                               '>>> test_dones = [False, False, True, False, False, True]\n'
                                               '>>> test_return_perpetuity = discounted_returns(test_rewards, test_dones, 0.5, perpetuity=True)\n'
                                               '>>> actual_return_perpetuity = np.array([3.5, 5., 6., 5.5, 3., 2.])\n'
                                               '>>> assert_equal(test_return_perpetuity, actual_return_perpetuity)\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> assert_equal = functools.partial(torch.testing.assert_close, rtol=1e-5, atol=0)\n'
                                               '>>> _other_discount = 0.8\n'
                                               '>>> _other_rewards = [2.0, 3.0, 1.0, 4.0, 5.0, 6.0]\n'
                                               '>>> _other_dones = [False, True, False, True, False, True]\n'
                                               '>>> _other_returns_true = np.array([4.4, 3.0, 4.2, 4.0, 9.8, 6.0])\n'
                                               '>>> _other_returns_pred = discounted_returns(_other_rewards, _other_dones, _other_discount)\n'
                                               '>>> assert_equal(_other_returns_pred, _other_returns_true)\n',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> assert_equal = functools.partial(torch.testing.assert_close, rtol=1e-5, atol=0)\n'
                                               '>>> _other_discount = 0.8\n'
                                               '>>> _other_rewards = [2.0, 3.0, 1.0, 4.0, 5.0, 6.0]\n'
                                               '>>> _other_dones = [False, True, False, True, False, True]\n'
                                               '>>> _other_returns_perp_true = np.array([14., 15., 17., 20., 29., 30.])\n'
                                               '>>> _other_returns_perp_pred = discounted_returns(_other_rewards, _other_dones, _other_discount, perpetuity=True)\n'
                                               '>>> assert_equal(_other_returns_perp_pred, _other_returns_perp_true)\n',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
