OK_FORMAT = True

test = {   'name': 'question 3b',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': ">>> test_env = gym.make('CartPole-v0')\n"
                                               '>>> test_state = test_env.reset()\n'
                                               '>>> test_value_net = value_init_network(test_env)\n'
                                               '>>> test_value = test_value_net(torch.FloatTensor(test_state))\n'
                                               '>>> np.testing.assert_allclose(test_value.shape[0], 1)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
