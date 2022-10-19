OK_FORMAT = True

test = {   'name': 'question 1a',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': ">>> test_env = gym.make('CartPole-v0')\n"
                                               '>>> test_output = policy_init_network(test_env)\n'
                                               '>>> test_state = torch.tensor([-0.04, 0.02, -0.04, 0.02])\n'
                                               '>>> test_out = test_output(test_state)\n'
                                               '>>> np.testing.assert_allclose(test_out.shape[0], 2)\n'
                                               '>>> np.testing.assert_allclose(test_out.detach().numpy().sum(), 1.0, rtol=1e-5, atol=0)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
