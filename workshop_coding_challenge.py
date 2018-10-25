import gym
import numpy as np

env = gym.make('Breakout-ram-v4')

print(env.unwrapped.get_action_meanings())

for epoch in range(20):
    env.reset()
    
    while True:
        obs, reward, is_done, infos = env.step(env.action_space.sample())
        env.render()
        
        ram = np.asarray(obs)
        
        print('observations:', ram)
        print('reward:', reward)
        print('debug informations:', infos)
        
        
        if is_done:
            break
            
env.close()
