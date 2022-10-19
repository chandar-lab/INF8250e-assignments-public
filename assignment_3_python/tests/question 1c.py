OK_FORMAT = True

test = {   'name': 'question 1c',
    'points': [3, 3, 4],
    'suites': [   {   'cases': [   {   'code': '>>> import functools\n'
                                               '>>> assert_equal = functools.partial(torch.testing.assert_close, rtol=0, atol=0)\n'
                                               '>>> num_rollouts = 3\n'
                                               '>>> test_s, test_a, test_r, test_d = rollout(test_env, test_policy, num_rollouts)\n'
                                               '>>> test_len_rollout = test_s.shape[0]\n'
                                               '>>> assert_equal(isinstance(test_s, np.ndarray), True)\n'
                                               '>>> assert_equal(isinstance(test_a, np.ndarray), True)\n'
                                               '>>> assert_equal(isinstance(test_r, np.ndarray), True)\n'
                                               '>>> assert_equal(isinstance(test_d, np.ndarray), True)\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> assert_equal(test_s.shape, (test_len_rollout, 4))\n'
                                               '>>> assert_equal(test_a.shape, (test_len_rollout,))\n'
                                               '>>> assert_equal(test_r.shape, (test_len_rollout,))\n'
                                               '>>> assert_equal(test_d.shape, (test_len_rollout,))\n',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> assert_equal(np.any((test_a != 0)&(test_a != 1 )), False)\n>>> assert_equal(np.sum(test_d), num_rollouts)\n', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
