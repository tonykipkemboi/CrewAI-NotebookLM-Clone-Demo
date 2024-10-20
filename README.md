# 🤖📓🎧 CrewaiNotebooklmClone Crew

Welcome to the **CrewaiNotebooklmClone** project, powered by [CrewAI](https://crewai.com), [Cerebras](https://cerebras.ai), and [ElevenLabs](https://www.elevenlabs.io)!

This project showcases the capabilities of multi-agent collaboration for podcast production, demonstrating a complete workflow from script creation to audio generation.&#x20;

The goal is to enable you to easily set up a multi-agent system that works in unison to produce a podcast, showcasing the potential of integrating AI with practical creativity.

[Download Sample Podcast](https://github.com/tonykipkemboi/CrewAI-NotebookLM-Clone-Demo/blob/main/output/podcast_20241019_125508.mp3)

## 📖 Project Overview

**CrewaiNotebooklmClone** is a multi-agent AI system built to streamline the podcast production process. The agents in this project:

1. **Script Writing Agent**: Summarizes content and generates a two-speaker conversational script, making technical content more accessible and engaging.
2. **Audio Production Agent**: Converts the generated script into audio, utilizing natural-sounding voices for a lifelike experience.
3. **Podcast Merging Agent**: Merges the individual audio clips into a final podcast file, ready for publication.

This project effectively uses tools such as **Cerebras** for blazing fast inference using **Llama3.1-70B model** for language generation and **ElevenLabs API** for speech synthesis.

## 🛠️ Features

- **Conversational Script Writing**: Generates lively, engaging conversations between two podcast hosts, using Cerebras API.
- **Voice Synthesis**: Produces natural-sounding audio files for the generated script using ElevenLabs.
- **Audio Merging**: Merges individual audio segments into a cohesive podcast episode.
- **Flexible Configuration**: Easily modify agent and task configurations to customize outputs.

## 🚀 Running the Project

To initiate your crew of AI agents and start executing tasks, run the following command from the root directory:

1. First lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `CEREBRAS_API_KEY` & `ELEVENLABS_API_KEY` into the `.env` file**

- Modify `src/crewai_notebooklm_clone/config/agents.yaml` to define your agents
- Modify `src/crewai_notebooklm_clone/config/tasks.yaml` to define your tasks
- Modify `src/crewai_notebooklm_clone/crew.py` to add your own logic, tools and specific args
- Modify `src/crewai_notebooklm_clone/main.py` to add custom inputs for your agents and tasks

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command kicks off the **CrewaiNotebooklmClone** Crew, assembling the agents and assigning them tasks according to the configuration. In its default form, the crew will:

1. Summarize a provided text into key points.
2. Generate a podcast script featuring Chuckles (the technical host) and Giggles (the curious co-host).
3. Convert the script into audio files.
4. Merge the audio files into a final podcast episode.

## 🧠 Understanding the Agents and Tasks

This crew consists of three main agents, each with specific tasks:

1. **Summarizer and Conversational Script Writer**

   - **Role**: Senior Content Summarizer
   - **Goal**: Summarize content and create a conversational script for a podcast featuring two speakers.

2. **Audio Producer**

   - **Role**: Audio Producer
   - **Goal**: Convert the generated script into audio files using ElevenLabs.

3. **Podcast Audio Producer**

   - **Role**: Podcast Audio Producer
   - **Goal**: Merge the individual audio clips into a final podcast episode.

The collaboration between these agents enables a smooth workflow from concept to audio production.

## 🧰 Customizing the Workflow

To tailor the workflow for your specific needs, you can:

- Modify the `agents.yaml` and `tasks.yaml` configuration files.
- Update the script writing prompts in `custom_tool.py` to adjust the tone or style of the generated podcast content.
- Integrate additional tools if necessary to expand the capabilities of your crew.

## 🎗️ Support and Community

For any questions, feedback, or support, feel free to reach out:

- Visit the [CrewAI Documentation](https://docs.crewai.com) for detailed guides and references.
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb) to engage with the CrewAI community.
- For any issues or contributions, check out the [GitHub repository](https://github.com/joaomdmoura/crewai).
- Follow me on X [@tonykipkemboi]\([https://www.x.com/tonykipkemboi](https://www.x.com/tonykipkemboi))
