OK_FORMAT = True

test = {   'name': 'question 4b',
    'points': [2, 3],
    'suites': [   {   'cases': [   {   'code': '>>> assert_equal = functools.partial(torch.testing.assert_close, rtol=0, atol=0)\n'
                                               ">>> test_env = gym.make('CartPole-v0')\n"
                                               '>>> test_value_net = value_init_network(test_env)\n'
                                               '>>> test_actor_critic = ActorCriticPolicy(test_env, policy_init_network(test_env), test_value_net,0.99)\n'
                                               '>>> loss = test_actor_critic.train_episode()\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> assert_equal = functools.partial(torch.testing.assert_close, rtol=0, atol=0)\n'
                                               ">>> test_env = gym.make('CartPole-v0')\n"
                                               '>>> test_value_net = value_init_network(test_env)\n'
                                               '>>> test_actor_critic = ActorCriticPolicy(test_env, policy_init_network(test_env), test_value_net,0.99)\n'
                                               '>>> loss = test_actor_critic.train_episode()\n'
                                               '>>> assert_equal(isinstance(loss,dict), True)\n'
                                               ">>> assert_equal('policy_loss' in loss, True)\n"
                                               ">>> assert_equal('value_loss' in loss, True)\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
