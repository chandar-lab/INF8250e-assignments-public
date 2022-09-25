test = {   'name': 'question 1.2b',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> dummy_states = [0, 5, 0, 0, 0, 0, 5, 0, 5, 0, 0, 0, 5, 0, 0, 5, 5]\n'
                                               '>>> dummy_actions = [1, 3, 0, 0, 3, 1, 3, 1, 3, 0, 0, 1, 0, 3, 1, 0]\n'
                                               '>>> dummy_rewards = [-1, -1, -1, -1, -1, -1, -1, -10, -1, -100, -1, -1, -1, -1, -1, -1]\n'
                                               '>>> \n'
                                               '>>> dummy_state_action_values = np.ones((12, 4))\n'
                                               '>>> dummy_state_action_values[:, 0] = 10\n'
                                               '>>> dummy_target_policy = make_eps_greedy_policy_distribution(dummy_state_action_values, epsilon=0.3)\n'
                                               '>>> \n'
                                               '>>> predicted_answer = is_mc_estimate_with_ratios(dummy_states, dummy_actions,\n'
                                               '...                                               dummy_rewards, dummy_target_policy, discount=0.99)\n'
                                               '>>> \n'
                                               '>>> np.testing.assert_allclose(len(predicted_answer.keys()), 2) # Only two distinct states \n'
                                               '...                                                             #are visited in the dummy episode\n'
                                               '>>> np.testing.assert_allclose(len(predicted_answer[0]), 11) # State 0 is visited 11 ttimes\n'
                                               '>>> \n'
                                               '>>> # Make sure lengths and types are correct\n'
                                               '>>> for k in predicted_answer:\n'
                                               '...     assert type(predicted_answer[k]) == list\n'
                                               '...     assert type(predicted_answer[k][0]) == tuple\n'
                                               '...     assert len(predicted_answer[k][0]) == 2\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> answer = {0: [(-2.980232238769531, 0.029802322387695312),\n'
                                               '...   (-2.3841857910156246, 0.02384185791015625),\n'
                                               '...   (-4.76837158203125, 0.0476837158203125),\n'
                                               '...   (-9.5367431640625, 0.095367431640625),\n'
                                               '...   (-19.073486328125, 0.19073486328125),\n'
                                               '...   (-15.2587890625, 0.152587890625),\n'
                                               '...   (-12.207031249999998, 0.1220703125),\n'
                                               '...   (-24.4140625, 0.244140625),\n'
                                               '...   (-48.828125, 0.48828125),\n'
                                               '...   (-39.0625, 0.390625),\n'
                                               '...   (-78.125, 0.78125)],\n'
                                               '...  5: [(-1.1920928955078125, 0.011920928955078125),\n'
                                               '...   (-7.62939453125, 0.0762939453125),\n'
                                               '...   (-6.103515624999999, 0.06103515625),\n'
                                               '...   (-19.53125, 0.1953125),\n'
                                               '...   (-31.25, 0.3125),\n'
                                               '...   (-62.49999999999999, 0.625)],\n'
                                               '...  6: [(-125.0, 1.25)],\n'
                                               '...  11: [(-50.0, 0.5)]}\n'
                                               '>>> \n'
                                               '>>> dummy_states = [0, 5, 0, 0, 0, 0, 5, 0, 5, 0, 0, 0, 5, 0, 0, 5, 5, 6, 11, 11]\n'
                                               '>>> dummy_actions = [1, 3, 0, 0, 3, 1, 3, 1, 3, 0, 0, 1, 0, 3, 1, 0, 2, 1, 2]\n'
                                               '>>> dummy_rewards = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -100]\n'
                                               '>>> \n'
                                               '>>> dummy_state_action_values = np.ones((12, 4))\n'
                                               '>>> dummy_state_action_values[:, 1] = 10\n'
                                               '>>> dummy_target_policy = make_eps_greedy_policy_distribution(dummy_state_action_values, epsilon=0.5)\n'
                                               '>>> \n'
                                               '>>> predicted_answer = is_mc_estimate_with_ratios(dummy_states, dummy_actions,\n'
                                               '...                                               dummy_rewards, dummy_target_policy, discount=0.99)\n'
                                               '>>> \n'
                                               '>>> for s in answer:\n'
                                               '...     np.testing.assert_allclose(answer[s], predicted_answer[s])\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
