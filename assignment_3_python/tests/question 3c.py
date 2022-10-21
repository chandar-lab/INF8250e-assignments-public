OK_FORMAT = True

test = {   'name': 'question 3c',
    'points': [1, 1, 1],
    'suites': [   {   'cases': [   {   'code': '>>> assert_equal = functools.partial(torch.testing.assert_close, rtol=0, atol=0)\n'
                                               ">>> test_env = gym.make('CartPole-v0')\n"
                                               '>>> test_value_net = value_init_network(test_env)\n'
                                               '>>> test_state = torch.tensor([-0.04, 0.02, -0.04, 0.02])\n'
                                               '>>> test_reinforce_baseline = REINFORCEWithBaselinePolicy(test_env, policy_init_network(test_env), test_value_net,0.99)\n'
                                               '>>> assert_equal(isinstance(test_reinforce_baseline.value_opt, torch.optim.Optimizer), True)\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> assert_equal = functools.partial(torch.testing.assert_close, rtol=0, atol=0)\n'
                                               ">>> test_env = gym.make('CartPole-v0')\n"
                                               '>>> test_value_net = value_init_network(test_env)\n'
                                               '>>> test_state = torch.tensor([-0.04, 0.02, -0.04, 0.02])\n'
                                               '>>> test_reinforce_baseline = REINFORCEWithBaselinePolicy(test_env, policy_init_network(test_env), test_value_net,0.99)\n'
                                               '>>> test_states, test_actions, test_rewards, test_dones = rollout(test_env, test_reinforce_baseline, 2)\n'
                                               '>>> loss = test_reinforce_baseline.update(test_states, test_actions, test_rewards, test_dones)\n'
                                               '>>> assert_equal(isinstance(loss,dict), True)\n'
                                               ">>> assert_equal('policy_loss' in loss, True)\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> assert_equal = functools.partial(torch.testing.assert_close, rtol=0, atol=0)\n'
                                               ">>> test_env = gym.make('CartPole-v0')\n"
                                               '>>> test_value_net = value_init_network(test_env)\n'
                                               '>>> test_state = torch.tensor([-0.04, 0.02, -0.04, 0.02])\n'
                                               '>>> test_reinforce_baseline = REINFORCEWithBaselinePolicy(test_env, policy_init_network(test_env), test_value_net,0.99)\n'
                                               '>>> test_states, test_actions, test_rewards, test_dones = rollout(test_env, test_reinforce_baseline, 2)\n'
                                               '>>> loss = test_reinforce_baseline.update(test_states, test_actions, test_rewards, test_dones)\n'
                                               ">>> assert_equal('value_loss' in loss, True)\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
