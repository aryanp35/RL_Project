from rl_coach.agents.ddpg_agent import DDPGAgentParameters
from rl_coach.base_parameters import VisualizationParameters
from rl_coach.core_types import TrainingSteps, EnvironmentEpisodes, EnvironmentSteps
from rl_coach.environments.carla_environment import CarlaEnvironmentParameters
from rl_coach.graph_managers.basic_rl_graph_manager import BasicRLGraphManager
from rl_coach.graph_managers.graph_manager import ScheduleParameters

####################
# Graph Scheduling #
####################
schedule_params = ScheduleParameters()
schedule_params.improve_steps = TrainingSteps(10000000000)
schedule_params.steps_between_evaluation_periods = EnvironmentEpisodes(20)
schedule_params.evaluation_steps = EnvironmentEpisodes(1)
schedule_params.heatup_steps = EnvironmentSteps(1000)

#########
# Agent #
#########
agent_params = ActorCriticAgentParameters()
agent_params.algorithm.apply_gradients_every_x_episodes = 1
agent_params.algorithm.num_steps_between_gradient_updates = 10000000
agent_params.algorithm.beta_entropy = 0.0001
agent_params.network_wrappers['main'].learning_rate = 0.00001

agent_params.input_filter = InputFilter()
agent_params.input_filter.add_reward_filter('rescale', RewardRescaleFilter(1/20.))
agent_params.input_filter.add_observation_filter('observation', 'normalize', ObservationNormalizationFilter())

###############
# Environment #
###############
env_params = CarlaEnvironmentParameters()

graph_manager = BasicRLGraphManager(agent_params=agent_params, env_params=env_params,
                                    schedule_params=schedule_params, vis_params=VisualizationParameters())