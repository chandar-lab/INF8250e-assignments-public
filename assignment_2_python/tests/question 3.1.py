test = {   'name': 'question 3.1',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> class DummyAgent(Agent):\n'
                                               '...     \n'
                                               '...     def agent_step(self, prev_state, prev_action, prev_reward, current_state, done):\n'
                                               '...         """ A learning step for the agent given SARS\n'
                                               '...         Args:\n'
                                               '...             prev_state (int): the state observation from the enviromnents last step\n'
                                               '...             prev_action (int): the action taken given prev_state\n'
                                               '...             prev_reward (float): The reward received for taking prev_action in prev_state\n'
                                               '...             current_state (int): The state received for taking prev_action in prev_state\n'
                                               '...             done (bool): Indicator that the episode is done \n'
                                               '...         Returns: \n'
                                               '...             action (int): the action the agent is taking given current_state\n'
                                               '...         """\n'
                                               '...         return 1\n'
                                               '>>> env = FrozenLakeEnv(map_name="6x5", slip_rate=0.)\n'
                                               '>>> agent_info = {\n'
                                               '...         "num_actions": 4,\n'
                                               '...         "num_states": 30,\n'
                                               '...         "epsilon": 0.,\n'
                                               '...         "step_size": 0.1,\n'
                                               '...         "discount": 0.99,\n'
                                               '...         "seed": 0\n'
                                               '...         }\n'
                                               '>>> dummy_agent = DummyAgent()\n'
                                               '>>> dummy_agent.agent_init(agent_info)\n'
                                               '>>> \n'
                                               '>>> s_true, a_true, r_true = [0, 0, 5, 10, 15, 20, 25, 25], [0, 1, 1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1, 0]\n'
                                               '>>> s, a, r = train_episode(dummy_agent, env)\n'
                                               '>>> np.testing.assert_allclose(s, s_true)\n'
                                               '>>> np.testing.assert_allclose(a, a_true)\n'
                                               '>>> np.testing.assert_allclose(r, r_true)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
