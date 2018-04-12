from environment import Simulator
from agent import PolicyGradientAgent, CriticsAgent
import datetime as dt
import numpy as np
def main():
    rule = {'Finance':['price_ICBC','price_taibao'], 'Electrical Engineering':['ee_600482','ee_600560'],
            'Real Estate':['housing_600240','housing_600743'],'Bio Medicine':['bio_600436','bio_600566']}


    def trade(pair,tick,iter):

        actions = ["buy", "sell", "hold"]

        n_iter = iter
        env_train = Simulator(pair, dt.datetime(2014, 10, 9), dt.datetime(2017, 10,30))
        agent = PolicyGradientAgent(lookback=env_train.init_state())

        for i in range(n_iter):

            env_train = Simulator(pair, dt.datetime(2014, 10, 9), dt.datetime(2017, 10,30))

            agent.reset(lookback=env_train.init_state())
            #critic_agent = CriticsAgent(lookback=env.init_state())
            action = agent.init_query()


            while env_train.has_more():
                action = actions[action]
                print("#########Runner: Taking action################", env_train.date, action)
                reward, state = env_train.step(action)
                action = agent.query(state, reward)

            if i == n_iter - 1:
                env_train.visualize(item,n_iter,'In Sample')


        env_test = Simulator(pair, dt.datetime(2017, 10, 30), dt.datetime(2018, 4, 10))
        agent.reset(lookback=env_test.init_state())
        while env_test.has_more():
            action = actions[action] # map action from id to name
            print("#############################################################")
            print ("Runner Test: Taking action", env_test.date, action)
            print("##########################################################")
            reward, state = env_test.step(action)
            action = agent.query(state, reward)

        env_test.visualize(item,n_iter, 'Out Sample')

    for iter in [1,10,20]:
        for item in rule:
            trade(rule[item],item, iter)


if __name__ == '__main__':
    main()
