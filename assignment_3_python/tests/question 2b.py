OK_FORMAT = True

test = {   'name': 'question 2b',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': ">>> test_env = gym.make('CartPole-v0')\n"
                                               '>>> assert_equal = functools.partial(torch.testing.assert_close, rtol=0, atol=0)\n'
                                               '>>> test_reinforce = REINFORCEPolicy(test_env, policy_init_network(test_env), 0.99)\n'
                                               '>>> test_states, test_actions, test_rewards, test_dones = rollout(test_env, test_reinforce, 2)\n'
                                               '>>> loss = test_reinforce.update(test_states, test_actions, test_rewards, test_dones)\n'
                                               '>>> assert_equal(isinstance(loss,dict), True)\n'
                                               ">>> assert_equal('policy_loss' in loss, True)\n"
                                               ">>> assert_equal(isinstance(loss['policy_loss'], float), True)\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
