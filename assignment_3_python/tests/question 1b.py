OK_FORMAT = True

test = {   'name': 'question 1b',
    'points': [5, 5, 5],
    'suites': [   {   'cases': [   {   'code': '>>> test_state = env.reset()\n'
                                               '>>> assert_equal = functools.partial(torch.testing.assert_close, rtol=0, atol=0)\n'
                                               '>>> test_policy = Policy(env, policy_init_network(env), 0.99)\n'
                                               '>>> assert_equal(isinstance(test_policy.opt, torch.optim.Optimizer), True)\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> test_state = env.reset()\n'
                                               '>>> test_policy = Policy(env, policy_init_network(env), 0.99)\n'
                                               '>>> assert_equal = functools.partial(torch.testing.assert_close, rtol=0, atol=0)\n'
                                               '>>> assert_equal(isinstance(test_policy.dist(test_state).param_shape, torch.Size), True)\n'
                                               '>>> assert_equal(test_policy.dist(test_state).param_shape, torch.Size([1,2]))\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> assert_equal = functools.partial(torch.testing.assert_close, rtol=0, atol=0)\n'
                                               '>>> test_state = env.reset()\n'
                                               '>>> test_policy = Policy(env, policy_init_network(env), 0.99)\n'
                                               '>>> assert_equal(isinstance(test_policy.dist(test_state), torch.distributions.Categorical), True)\n'
                                               '>>> assert_equal(test_policy.action(test_state) in [0,1], True)\n',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
