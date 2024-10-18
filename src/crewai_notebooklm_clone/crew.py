import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_notebooklm_clone.tools.custom_tool import CerebrasTool, ElevenLabsTool, MergeAudioTool

llm = LLM(
    model="cerebras/llama3.1-70b",
    base_url="https://api.cerebras.ai/v1",
    api_key=os.getenv("CEREBRAS_API_KEY"),
	temperature=0
)

@CrewBase
class CrewaiNotebooklmCloneCrew():
	"""CrewaiNotebooklmClone crew"""

	@agent
	def summarizer_and_conversational_script_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['summarizer_and_conversational_script_writer'],
			verbose=True,
			tools=[CerebrasTool()],
			llm=llm
		)

	@agent
	def audio_producer(self) -> Agent:
		return Agent(
			config=self.agents_config['audio_producer'],
			verbose=True,
			tools=[ElevenLabsTool()],
			llm=llm
		)

	@agent
	def podcast_audio_producer(self) -> Agent:
		return Agent(
			config=self.agents_config['podcast_audio_producer'],
			verbose=True,
			tools=[MergeAudioTool()],
			llm=llm
		)

	@task
	def summarizer_and_conversational_script_writer_task(self) -> Task:
		return Task(
			config=self.tasks_config['summarizer_and_conversational_script_writer_task'],
			output_file='output/script.json'	
		)

	@task
	def audio_producer_task(self) -> Task:
		return Task(
			config=self.tasks_config['audio_producer_task'],
		)

	@task
	def podcast_audio_producer_task(self) -> Task:
		return Task(
			config=self.tasks_config['podcast_audio_producer_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CrewaiNotebooklmClone crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)