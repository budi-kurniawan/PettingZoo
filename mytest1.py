from pettingzoo.butterfly import pistonball_v3

if __name__ == '__main__':
    env = pistonball_v3.env()
    print('env type:', type(env), env)
    env.reset()
    print('agents:', env.agents, ", len:", len(env.agents))
    print('agent selection type:' , type(env.agent_selection), env.agent_selection)
    print('action spaces:', type(env.action_spaces), env.action_spaces)
    print('len action spaces:', len(env.action_spaces))
    
    for agent in env.agent_iter(1000):
        print('agent:', agent) # print 'piston_x' where x is [0..19]
        observation, reward, done, info = env.last()
        env.render()
        num_actions = len(env.action_spaces)
        action = env.action_spaces[agent].sample() # type(action) is an array of one element
        env.step(action)
