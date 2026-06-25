# 📝 Notes

Aug 13, 2025

## 8am AI\!

Invited [David Olsson](mailto:david@atomic47.co) [eric@scroll.ca](mailto:eric@scroll.ca) [James Giroday](mailto:giroday@gmail.com) [Hanif Janmohamed](mailto:hanif.janmohamed@gmail.com) [Scott Morton](mailto:scott@driftresourcetechnologies.com) [Anshul Dhariwal](mailto:anshuldhariwal04@gmail.com) [Travis Worthing](mailto:travis@atomic47.co) [Bibi Souza](mailto:bibi@atomic47.co) [Jason Kryski](mailto:jason@mttr.ca) [Jen Boger](mailto:jen@atomic47.co) [Myles Holt](mailto:myles@mttr.ca) [Loren Kuich](mailto:loren@mttr.ca) [Shabraj Shahid](mailto:shabraj@mttr.ca) [Ashley Beckett](mailto:ashley@mttr.ca) [graham@ratiomachina.com](mailto:graham@ratiomachina.com) ~~[Fulvio Ciano](mailto:fulvio@atomic47.co)~~ ~~[spencer@ratiomachina.com](mailto:spencer@ratiomachina.com)~~

Attachments [8am AI\!](https://www.google.com/calendar/event?eid=aW52N2w4MWJvNjJqYm5zYmQxZTMzYjllNmZfMjAyNTA4MTNUMTUwMDAwWiBkYXZpZEBhdG9taWM0Ny5jbw) 

Meeting records [Transcript](?tab=t.axydyslzl4g5) 

### Summary

David Olsson and Myles Holt discussed integrating AI tools into Git repositories for documentation and code review, with David Olsson showcasing how agents can generate READMEs and technical specifications while using GitHub for long-term memory. James Giroday, David Olsson, and Myles Holt explored structuring meetings, using GitHub for transcript management, and the broader motivation for parsing transcripts to leverage them as an asset for knowledge mining. James Giroday, with strong support from Myles Holt and David Olsson, proposed and voted to experiment with a dedicated 20-minute demo slot in future meetings, while Jen Boger and David Olsson considered adding labels to call titles for better organization.

### Details

* **AI in Git Repositories** Myles Holt asked about using cloud code in Git repositories for AI purposes. David Olsson shared insights on AI tools like Jules's tool from Google and Cursor's agents, which operate within the IDE. He explained that these agents can self-propagate and teach themselves by checking their own code, essentially using Git as memory to advance and build their own tools.

* **Agent Capabilities and Use Cases** David Olsson discussed the extensive use of cloud code agents, mentioning the creation of "teams" of agents that can be used inside cloud code or the desktop environment. He highlighted their keenness on using these agents for documentation and maintaining context between code and documentation ([00:02:11](#00:02:11)). Myles Holt expressed curiosity about the feedback provided by agents during code reviews, particularly regarding Claude's ability to perform such reviews ([00:03:06](#00:03:06)).

* **Agent-Driven Documentation and Website Generation** David Olsson demonstrated the practical application of agents by recounting how they used agents to process a directory of repositories, generating READMEs and technical specifications for 80-120 files or applications. They also described getting the agents to use Playwright to load apps, take screenshots, and build an index web page. David Olsson stated that using Claude inside Cursor is the easiest way to achieve this ([00:04:05](#00:04:05)).

* **GitHub for Long-Term Memory and Reconciliation** David Olsson introduced the concept of using GitHub as a memory component for projects, leveraging Git's check-in capabilities for reconciliation and long-term memory through pull requests ([00:05:03](#00:05:03)). They elaborated on how agents can be integrated into projects, maintaining their memory within the project through markdown files, which also serve as a workflow guide ([00:05:54](#00:05:54)). This approach provides visibility into ongoing activities and allows for easy prompting of specialized agents ([00:06:48](#00:06:48)).

* **Transcripts and the Master Control Program (MCP)** David Olsson shared their progress on utilizing an MCP installed in the cloud desktop to process meeting transcripts. They explained that the MCP could summarize and highlight information from 50 weeks' worth of transcripts, aiming to install it into Cursor to enable querying of downloadable transcripts directly through prompts ([00:07:47](#00:07:47)). James Giroday inquired about the location and nature of this MCP ([00:08:50](#00:08:50)).

* **MCP Configuration and Security** David Olsson explained that the MCP is a JSON configuration file that sits within another MCP configuration file and requires a key to access their Fireflies account ([00:08:50](#00:08:50)). They acknowledged the security challenges associated with managing such keys. David Olsson noted that their Cloud account allows for configuring various MCPs, some of which are open source or can connect to other accounts like Google ([00:09:44](#00:09:44)).

* **Meeting Structure and Workshop Improvements** James Giroday initiated a discussion on structuring the 8 a.m. meetings, suggesting a balance between informal "sideways thinking" and more structured elements like dedicated demo windows ([00:10:39](#00:10:39)). They proposed giving advance notice for demo presentations to make it more approachable for participants ([00:11:42](#00:11:42)). David Olsson shared their team's experience at Atomic 47, where a simple document-based schedule helped organize writing tasks with minimal, yet effective, structure ([00:13:05](#00:13:05)).

* **GitHub for Change Management and Transcript Storage** James Giroday proposed using GitHub for change management and version control, particularly for meeting transcripts, recognizing its existing software-based collaboration features ([00:13:59](#00:13:59)). David Olsson affirmed this idea, stating that GitHub is a free and suitable platform where an MCP can automatically move transcripts into a repo ([00:15:07](#00:15:07)). They also noted that GitHub's permissions and actions allow for controlled access and agent-based processing of the content ([00:16:30](#00:16:30)).

* **Transcript Storage and Access Challenges** David Olsson explained that they currently download and process Fireflies transcripts manually due to the cost and limitations of Fireflies' built-in agents. They emphasized the importance of integrating Fireflies' API with a more open system like GitHub to free the information from being locked into their account and system ([00:17:37](#00:17:37)). David Olsson highlighted that an MCP can facilitate this process, allowing everyone to access the repo by adding the GitHub MCP to their cloud desktop ([00:18:57](#00:18:57)).

* **Pipeline for Transcript Management** James Giroday sought clarification on the technical stack and process for handling transcripts, suggesting a pipeline involving Fireflies, Cursor, and cloud code with an MCP. David Olsson clarified that the MCP assists with transporting files from Fireflies to either a desktop or server, and they would manually prompt Cursor to download transcripts and audio files into a GitHub repository ([00:19:54](#00:19:54)) ([00:34:01](#00:34:01)). They also envisioned an automated pipeline that would eventually bypass manual intervention, pushing files directly to GitHub from a server using cron jobs or triggers ([00:37:47](#00:37:47)).

* **Account Setup for Transcript Management** James Giroday asked David Olsson to outline the necessary accounts for setting up this transcript management system ([00:20:51](#00:20:51)). David Olsson explained that a GitHub account is needed to store information, and an email and phone number (preferably a Google account) are generally required. For meeting transcripts, integration with a meeting software like Fireflies, which has an API to export transcripts to GitHub, is essential ([00:21:43](#00:21:43)). David Olsson mentioned that while Fireflies has been their choice, other services like Fathom might offer superior summaries and APIs ([00:22:35](#00:22:35)).

* **Automation Tools and Federated Identities** David Olsson suggested using tools like Zapier for those without coding proficiency to automate the transfer of transcripts from Fireflies to GitHub ([00:23:31](#00:23:31)). They acknowledged that such programmatic solutions often have limitations based on payment tiers ([00:25:51](#00:25:51)). The discussion also touched upon the complexities of "federated identities" (OAUTH), where multiple users log in with different IDs, making a single-account setup with a dedicated meeting scheduler more straightforward for automated processes ([00:26:57](#00:26:57)).

* **Motivation for Transcript Parsing** Myles Holt inquired about the motivation behind parsing transcripts, asking if it was an experiment or for a larger business case ([00:38:50](#00:38:50)). David Olsson explained that the project aims to leverage meeting transcripts as an asset, allowing multiple agents (a "curiosity council") to analyze them from different perspectives, identify themes, and stitch together patterns ([00:39:52](#00:39:52)). They described this as a "tertiary piece" to the core effort, focusing on knowledge mining and quality control to support self-improvement ([00:40:43](#00:40:43)).

* **Value of Accessible Transcripts** James Giroday emphasized the value of accessible meeting transcripts as a resource for collective curiosity and knowledge mining, enabling participants to look back, synthesize ideas, and understand workflows ([00:40:43](#00:40:43)). Myles Holt agreed on the value, suggesting that agents could perform secondary passes on topics for "curiosity exploration" and proposing a feedback loop to summarize these results for future meetings ([00:41:57](#00:41:57)).

* **Leveraging Corpus for Business Insights** David Olsson elaborated on how having a corpus of documented work, such as technical specs and READMEs, allows for deeper analysis by business and marketing agents ([00:44:03](#00:44:03)). They explained that this process helps uncover principles and values that drive business models, leading to a better understanding and new language around consistency and pathways ([00:45:12](#00:45:12)). David Olsson highlighted that with a well-structured corpus, one can trace ideas and identify synergies between projects ([00:46:04](#00:46:04)).

* **Project Management and Learning** David Olsson connected the transcript analysis to project management, suggesting that discussions within the meeting room, if well-cued with keywords, can trigger prompts and actions for project management without necessarily hiring a project manager ([00:47:11](#00:47:11)). James Giroday echoed this, stating that their personal motivation for participating is to learn about change management and how to action agents, viewing these as marketable skills ([00:48:09](#00:48:09)).

* **Publishing and Future Applications** David Olsson confirmed their intention to continue the initiative of placing transcripts into a GitHub repository and potentially publishing them ([00:50:26](#00:50:26)). They envisioned that having this historical data would allow for asking interesting questions of past meetings and that each past meeting could serve as a "unit test" for the current one ([00:51:35](#00:51:35)).

* **Demo Experiment and Voting** James Giroday proposed an experiment to reserve 20 minutes in future meetings for a demo, consisting of 10 minutes for presentation and 10 minutes for Q\&A, with ample lead time provided. They conducted a vote on this proposal using a finger-showing scale from zero (strong opposition) to five (strong favor) ([00:52:25](#00:52:25)). Myles Holt and David Olsson expressed strong support for the idea ([00:53:27](#00:53:27)). James Giroday committed to sending out an email to the group to solicit presenters ([00:54:22](#00:54:22)).

* **Call Organization and Labeling** Jen Boger suggested organizing calls by adding labels beyond just the title to allow for better categorization and extraction of themes, especially for specific groups and recurring clients ([00:56:09](#00:56:09)). David Olsson agreed that tagging could be a secondary processing step, noting that it could help people manage their time better by providing more informative subject lines in emails. They decided to consider labels for a future discussion ([00:57:14](#00:57:14)).

### Suggested next steps

- [ ] James Giroday will send an email to the group today to ask if anyone wants to present something for 20 minutes (10 minutes of presentation, 10 minutes of Q\&A) next week.  
- [ ] David Olsson will make sure that the transcript of the meeting is available for the group.

*You should review Gemini's notes to make sure they're accurate. [Get tips and learn how Gemini takes notes](https://support.google.com/meet/answer/14754931)*

*Please provide feedback about using Gemini to take notes in a [short survey.](https://google.qualtrics.com/jfe/form/SV_9vK3UZEaIQKKE7A?confid=HjiTKTLPBBBPIfT2D0MQDxISOAIIigIgABgBCA&detailid=unspecified)*

# 📖 Transcript

Aug 13, 2025

## 8am AI\! \- Transcript

### 00:00:00

   
**Myles Holt:** Sit in front of a fan.  
**David Olsson:** Yeah. Yeah. Uh well, we get smoke today, so that's not good.  
**Myles Holt:** Uh on the AI front, are you guys uh using cloud code in your git repos?  
**David Olsson:** Um, so we we just had a really good discussion about the AI in your repo thing and um, uh, Fobio can't really I don't think you can make it today. Um, but he was playing around with Jules's uh, tool that Google has and it acts right in there. And I said, well, cursor has those agents and they'll do that and then there's background agents and they're right in the IDE now. like I haven't really used them much. Um, but I'm I'm relying on Git and GitHub for a lot of my thinking as infrastructure and substrate. And I've been able to use GitHub as a a means to um have a an agent self-propagate and teach itself because it checking its own code just using it as memory and then being able to advance and then  
   
 

### 00:00:57

   
**Myles Holt:** All right.  
**David Olsson:** it can build its own tools. Um, which is, you know, like, oh, that's it. That's too much. It's like it it just starts to like, okay, if you can give a leash, it'll go. Um, and so the discussion we've been having is like, where do you sit with that? Where where are you sitting with the fact that, you know, uh, Fio likes the IDE? He likes using client inside VS Code and he sees the files and he can see what's going on and he can intercept. These ones kind of work in the black box.  
**Myles Holt:** Yeah, I'm using um I use cursor which um is great for editing files and and getting some some depth um on the code patterns in in the repo.  
**David Olsson:** So So  
**Myles Holt:** Um, but I'd like to add the code review ability from Claude. Um, and it created itself a PR. I'm just going to share that with the team here shortly. But just wanted to get your your sense on uh having the agent it.  
   
 

### 00:02:11 {#00:02:11}

   
**Myles Holt:** Yeah.  
**David Olsson:** um I'm keen I'm using it extensively. I'm using cloud code agents. I've built a whole uh something called a teams. It's like a bunch of different teams and our agents so we can use them inside cloud code or a cle or inside uh the desktop um to do exactly what you're talking about. I'm keen on using it for documentation. Um, what we talked about yesterday was trying to see if we can keep build agents to keep us keep our context in line with our code so that we're so there's documenting as we're moving kind of thing and um, good morning everyone. I'm keen on that kind of thing.  
**Jason Kryski:** Thanks.  
**David Olsson:** So what you're talking about is is what we're playing with and what I want to do is not necessarily the actual coding itself though have workflows for doing that and it comes out and just like yeah it's kind of what we said.  
**Myles Holt:** Right.  
**David Olsson:** It's just like no it's not really doing man.  
**Myles Holt:** Yeah.  
   
 

### 00:03:06 {#00:03:06}

   
**Myles Holt:** Yeah.  
**David Olsson:** So being the human in the middle like doing the code is still quite gratifying even if you have like a bunch of sub agents doing it. Um but that's the pattern we're looking at now is like okay I'm driving it here. I can have sub agents. I can get them doing that. And now with this pattern in place, I can just prompt saying use the planner and then use these other guys to collaborate and it'll figure it out. Like the claude will figure it out. It'll do the orchestration piece now. Um or you can give it a workflow and it'll actually follow that too. So, it's really quite cool with what you're talking about and I'd like to see how you're doing it because it's pretty scatter uh like uh shotgun blasting right now trying to figure this out.  
**Myles Holt:** Yeah, I'm sort of curious what kind of feedback it's going to give on code reviews because my understanding is that it can actually, you know, you ask it to do a code review on your branch and um yeah, I haven't seen it yet, but I'm curious  
   
 

### 00:04:05 {#00:04:05}

   
**David Olsson:** So, I had to go through a whole directory of repos. Turns out it was like 100 or 80 120 different uh files or apps and got it to write a read me a technical spec and then uh I figured out how to use playright and so it went in and loaded the apps and then took a screenshot of it and then I got it to build a index web page for me and so that's me figuring out how to have those agents do those works and and  
**Myles Holt:** Nice. Yeah.  
**David Olsson:** I'm using clot inside cursor to do that right now is the easiest way.  
**Myles Holt:** Okay.  
**David Olsson:** Cloud code cloud code inside cursor.  
**Myles Holt:** Yeah.  
**David Olsson:** Um but yeah, it it does its own thing and it is its own thing inside.  
**Myles Holt:** And you do that through the command prompt. Uh because I know the agent there's there's the agent tab. Uh and then you can specify a specific model. But when I put claw into that cursor, it wants to have its own um CLI interface through there.  
   
 

### 00:05:03 {#00:05:03}

   
**David Olsson:** So it doesn't integrate like you know the cursor agent's pretty good. Uh it's like if you run stuff in if you just run a prompt in there and just rely on the tools and say I have these tools it's you'll use the tools.  
**Myles Holt:** Yeah. And like you say, it likes to get a little bit uh run away sometimes and I have to scale it back. But yeah, I'll let you know how it goes with the GitHub stuff.  
**David Olsson:** So that's that's where um so we have the project called work sona and I was like thinking about this thing and we're trying to deal with memory and I'm like just markdown files like I'm looking at projects and you're just using markdown files and just you know there's just these simple patterns being put in place that are useful. Um and so I was looking at GitHub and seeing if I could just use it for the memory component because of just using git and and checkins and then reconciling. what you could do is you could do PRs to reconcile and have long-term memory.  
   
 

### 00:05:54 {#00:05:54}

   
**David Olsson:** Like it it worked out like, you know, short-term, midterm, long-term memory.  
**Myles Holt:** Right.  
**David Olsson:** Um, and then I'm like, well, what if you put the agent in there?  
**Myles Holt:** Yeah. Um I don't would it I guess it does have uh enough context to run itself.  
**David Olsson:** Yeah, they can deploy like if you give it um because it has actions, you can deploy it to any any any uh environment and then if you give it a manifest, it can figure out what environment it wants  
**Myles Holt:** Um yeah.  
**David Olsson:** to go into and then it'll figure out the code to do that.  
**Myles Holt:** Right.  
**David Olsson:** So that was like ah too too much. Um but that that pattern is really useful. In fact, the agents that I've built, you do an install process in your project. And this is this is an experiment to see how this goes. But you do an install in your project. You invite the agents in. You can customize them or you can build specific to the project too. Um and they work um inside the project and then they have their memory inside the project.  
   
 

### 00:06:48 {#00:06:48}

   
**David Olsson:** every time they do a report, it goes into memory and they have it's just a markdown file. So they have a shared memory through markdown and they have a workflow through markdown.  
**Myles Holt:** Right.  
**David Olsson:** And so it's really simple stuff, but it adds this level of visibility as to what's going on. And also if you just if you just prompt, it just does it. So if you if you're like, I need this and like, oh, I'll use the dock writer agent for that.  
**Myles Holt:** Yeah.  
**David Olsson:** I'm like, well, you wouldn't talk like that unless I put that in there. Um, so it relies on the fact that it now has claw does it relies on the fact it has 60 different agents that are specialized. It'll use them instead of just going off and doing stuff.  
**Myles Holt:** Yeah, it's very cool. We're um we're getting further down the re rabbit hole as we go as we progress. So,  
**David Olsson:** Yeah. And so what so this is kind of full circle. I I was wanting to get the repos or the the transcripts from last week uh and from the last turns out it's 50 weeks.  
   
 

### 00:07:47 {#00:07:47}

   
**David Olsson:** Um I think there's a couple more that I just had different names for. Um but I've installed the MCP into into cloud desktop and it will it doesn't want to do all 50 files of course. Um, but it did eventually build me a a table of contexts of like a a table of all of them and gave me a summary of all of them and gave me highlights for them. So, it did do some of the it looked at the summaries for them and then did that down. And so, I've been trying to install it into cursor um the MCP to into cursor because I did a session. And I'm like, "Okay, can I actually download the transcripts if I put the MCP inside um cursor?" I asked Claude that with the MCP installed like, "Can you answer this question?" And it said, "Yes, that's a really good use of it." And so, uh, so all the stuff I was building before, I'm like, screw that. I'll just prompt this, man. And, um, and and not even have a UI.  
   
 

### 00:08:50 {#00:08:50}

   
**David Olsson:** So, I've got an open directory and I'm like I'm trying to get the cursor thing working. I'm like I don't need anything in this directory. I'm just like download everything. Um, and it will throttle it. Meaning you can only do so many per minute. Um, and so that's the thing that I hope it manages all that. But it allowed for doing what I wanted to do and what I wanted to be able to give everybody the opportunity to do is like it's there as a corpus. You can now query it. It's still mechanical, right? you have to say I want a file or I want a not.  
**James Giroday:** Where is it? Can I Can I ask where is it?  
**David Olsson:** So what it is it's an MCP. So it's just it's like a configuration file that sits inside another it sits in a an MCP configuration file which is just JSON and then you just describe it. You put in one key of course and the key is very important and that's how everything in this world works is with keys.  
   
 

### 00:09:44 {#00:09:44}

   
**David Olsson:** They open the doors to everything and in this case it opens the door to my account and what it does. So security is like uh you know everybody's talking about security like this is the biggest black hole of security man where do you put that key right because eventually no it's my fireflies account so I have a cloud  
**James Giroday:** Which which account is it? Your claude account. Okay.  
**David Olsson:** account you have to have a cloud account to do these kind of things and then you can and then you can configure your claw desktop with a whole lot of different MCPs and a lot of them are just  
**James Giroday:** Yeah.  
**David Olsson:** like you just have an earl for it like it's just a and it's open and you use it. Um some of them you can get to accounts, right? So you can log into like you can Google you you can actually now you can I haven't done it and I'm like I don't know. Um you can connect your Google account to it so that you can like it'll see your scheduling and your Yeah.  
   
 

### 00:10:39 {#00:10:39}

   
**James Giroday:** Yeah. So, I can can I can I segue a little bit?  
**David Olsson:** Yeah. Yeah. Yeah.  
**James Giroday:** I've been So, I've been thinking about this a little uh a little bit on and off. Um I actually was talking with uh Graham as well and this has been like I think there's a conversation now that this is a thread that we've kind of been pulling at for like about a month. It's like the whole 8 a.m. thing. Like how do you how do you wrangle everything? How do you provide maybe a bit more structure? Maybe not. I don't know. Like part of the really nice thing about this meeting is that it's you just like showing up is the most fundamental thing and it's really easy. Like I find it easy. like it's an easy space to just sort of wade in and out of and there's not too much structure. It's I don't find it stifling at all which is nice. But the downside of that is like maybe the whole a you know workshop thing uh as you described David is like a little sideways.  
   
 

### 00:11:42 {#00:11:42}

   
**James Giroday:** It's just it's a lot of sideways thinking and stuff comes out of that. But if we want to provide some sort of a direction I've been chewing on this. I'm like how do you do it? And I was looking at like meeting formats. So everything down from like really informal to things like parliamentary procedure where there's like seconding and proposals and motions to X Y and Z. Um and I was like okay that's kind of interesting. Like okay how do you conduct a meeting? How do you conduct votes? Interesting things. Um, I mean another part of maybe structuring this workshop is like a little bit of both. Like we maybe set aside some time for the sideways stuff. We set aside like a little window for demos. Um because if we were to like set up demos and um reserve space for for people to share their stuff um that might be a little bit more uh maybe approachable for some like you to make it approachable. In fact, you'd need to give probably a bit of heads um like a bit of uh you know notice.  
   
 

### 00:13:05 {#00:13:05}

   
**James Giroday:** It's like okay like do you want a window to present something? you know, it can't be like, okay, like there's a window like who's got something. It's a little bit putting up people on the spot. So maybe you want to provide a bit more structure there. And then Mhm.  
**David Olsson:** So we we we we just started writing as a team at Atomic 47 and somebody Karen created a schedule and everybody's name was associated with it and you could edit it and move things around but it was a great place to start something like that. It was just a document and uh but minimal amount of structure. It does enough that everybody's like who's next?  
**James Giroday:** Oh yeah, a schedule.  
**David Olsson:** Yeah. So, but like we're like next Wednesday always happens.  
**James Giroday:** Yeah.  
**David Olsson:** Um and it could be like okay there's a there's a column that says topic and someone's got to fill it in. Well, we're so the same idea of trying to determine a path for writing.  
**James Giroday:** Yeah.  
   
 

### 00:13:59 {#00:13:59}

   
**James Giroday:** So, yeah. I mean, so you're you guys are experimenting with that a little bit.  
**David Olsson:** So, a little bit forced at the beginning saying here's some things to get started and then of course there'll be more interest in it and then you know because we're humans we can shuffle things around um with lightweight  
**James Giroday:** Yeah. Yeah.  
**David Olsson:** technology like a  
**James Giroday:** Totally. Yeah. like or um but so back to your back to your original point was like um how do you like where do you store this stuff in a secure place and what I was the two topics that I was starting to think about were like okay so change management is a topic that's something that I've kind of dealt with at work like that can go well or go badly when you introduce a new tool it's like oh how does this work and you know um and then like change control is like kind of close to version control which is GitHub and I feel like GitHub is actually a fairly I like I just think it's so  
   
 

### 00:15:07 {#00:15:07}

   
**David Olsson:** Yeah.  
**James Giroday:** brilliant like how you can collaborate on that platform because there the whole like way that change and versions are controlled is like softwarebased So if you can sum So then I was looking at like okay so if you were to get the transcripts onto GitHub how do you do that? Like what's the process? Like do you get consent? Do you set up like web hooks to sort of like grab it from a Google Drive and upload it? Like how do you Yeah. So, it's it's not it's not as simple maybe as like unless you want to sign up for like a pre, you know, a service like like what's what's that service that you  
**David Olsson:** So what's interesting is that you've kind of nailed a like a core set of things that we already have and can use and they can stitch out stitch together and then move out. Meaning GitHub is free and the MCP enables like a small app to every week just move the transcripts into the repo and then permissions are based on participation, right?  
   
 

### 00:16:30 {#00:16:30}

   
**David Olsson:** like you can make it a private repo, you can make it read only, you can do those things and then people can branch and they can do things and there's ways to have GitHub actions to act on it meaning we can have agents now GitHub has large language models accessible within its so it recognize what it can do too right so um so there's the ability to use it as a substrate um for a whole lot of things and in this case files it's a great place. I was I'm I immediately create a folder and create a GitHub repo now. And so this makes a lot of sense to this say, well, we can clone it. We can we can all have a copy and then you can you can do pull requests and stuff like that. And so the neat thing about it is it can be a primary set of information and then it can produce these secondary things and and move on and on in a closed or open loop there. So cool thinking, man. It aligns with what we started with last week and then what we've talked about today and even what Miles was bringing in. Um, so this is a I think that's a like out of the gate that's something that  
   
 

### 00:17:37 {#00:17:37}

   
**James Giroday:** Yeah. Yeah, definitely.  
**David Olsson:** I can do. Um, if this thing works in the background, that's something I can try right away because I could just say create a repo and then put like it's no effort to do that. I was gonna have to share somehow and uh it was going to be a question. My I putting things in uh Google Drive, but you know the agents not getting it's getting better and so that has value too. But um so right now I do it ad hoc.  
**Myles Holt:** What where are you currently storing the uh summary of the transcripts from Firefly?  
**David Olsson:** I I download them. So I started seeing a lot of value in processing about a year or longer ago. um but they have their own agents too that you can trigger and do special reports but they're they're costly and they're very small and so it's a matter of pulling things out or integrating with and that's one of the issues that we've been dealing with is like if we're going to do something in terms of changing our patterns and using these tools how do we you know what level do we integrate and how do we integrate in this case if we rely on the fact GitHub is there and it's just doing file stuff and however we transport from their system, meaning there is an API to export it into another more open system like a  
   
 

### 00:18:57 {#00:18:57}

   
**David Olsson:** GitHub. That's just a technical thing and we we could do it a number of ways. Turns out it's really easy to do with the new tools um like an MCP. So, um and that MCP has a lot of value and and then it means also that I could do something because it's my account, you know, so I'm a sponsor of that. I could then say, oh, it's a way of me freeing it up, right? the information is not locked into their system and to my account. And that's that was the first thing I wanted to do. And this is usually the first thing I do when we have a meeting that's meaningful. It's like take this. Now it happens automatically. Everybody gets a transcript. But if they're not in the meeting, we need to do that thing, pull it out, make a document, share the document. It's a lot of work. So um everybody can you know intro they can add a an M the u the GitHub MCP to desktop cloud desktop and then you could just access your repo that way.  
   
 

### 00:19:54 {#00:19:54}

   
**James Giroday:** Yeah. Okay. So, so David, can you take me through So, it sounds like we kind of agree like this would be a cool way to do it. Can you take me through it like I'm a five-year-old like what are what's the stack and how are you using it?  
**David Olsson:** Yeah. Well, as how about your So, as a So, there's two roles. There's a role that I would take right now as the sort of the sponsor of it, meaning that it's my account and I need to somehow share it. So, I would I would pick I would figure out how to take the file, the the transcript, and the audio just because we like that.  
**James Giroday:** sponsor. Uhhuh.  
**David Olsson:** um and then put them in a uh a directory inside a repo. And then the neat thing about GitHub is that we can we can share ownership and then people can invite people. And so it can be um easy to invite this room and people can get an account for free and the and and if we make it private that again can be a sponsorship thing from somebody that has the ability to do that.  
   
 

### 00:20:51 {#00:20:51}

   
**David Olsson:** But um we could also then discuss that, right?  
**James Giroday:** Okay.  
**David Olsson:** It has a wiki and it has all these other things too that if things become useful um but really what it does have is the ability to throw agents at it and make secondary research happen as a platform.  
**James Giroday:** All right. Sure. So before we get to that though, yeah, like the in the whole invite thing when you it seems so simple what we actually do on a daily basis when we're putting together a meeting, but like I see Yeah. So without sorry without getting the weeds, um let's say let's say you're starting from scratch, okay, you don't have any account whatsoever.  
**David Olsson:** So, how it would work is if so, yeah, you're in you get you get invited to this meeting somehow and then Okay.  
**James Giroday:** Take me through what you sign up for and then how you integrate it. Well, let's start with you. Let's start with you. like you don't have any accounts anywhere. So you go and you sign up for GitHub first, right?  
   
 

### 00:21:43 {#00:21:43}

   
**David Olsson:** Yeah. So I would need a GitHub account where I want to store some information.  
**James Giroday:** Yeah. All right. What uh and then do you need a Google account to sign up? I guess you need a Google account for for that. Probably probably signing Google.  
**David Olsson:** Uh you need email and you need and phone pretty much nowadays.  
**James Giroday:** Yeah. Yeah.  
**David Olsson:** You need to and if you don't have one, I would get a Google one.  
**James Giroday:** And then and then you sign up for is Firefly is the best one.  
**David Olsson:** But so I we've just been with Fireflies because at the time over two years ago it made sense and it has an API and so there's what you need to do is integrate with um whoever your meeting software  
**James Giroday:** Yeah.  
**David Olsson:** is will somehow have transcripts and you need to get those transcripts into GitHub.  
**James Giroday:** Okay.  
**David Olsson:** Um and so I don't think so but the API is is helpful.  
**James Giroday:** Do you think Fireflies is the best this at this time?  
   
 

### 00:22:35 {#00:22:35}

   
**James Giroday:** Yeah.  
**David Olsson:** Um and but I just had to upgrade to get the a access to the API. So you know um yeah know and it was just it's sorry.  
**James Giroday:** Nothing free.  
**Jason Kryski:** No, but they also  
**James Giroday:** I was look I was looking at Otter and uh I mean the the summaries that Fathom produced were like in my opinion far superior to Fireflies.  
**David Olsson:** Yeah. Right. And so they they should all have an API that allows you to get access to your um and so that would be something I would just use one of these LLMs to do is like do a comparison say maybe perplexity do a comparison which one gives you what you want. Are you concerned about security where it resides? All the other things is it price point is it API and in this case API is most important because I've used their system and it's terrible. um you're locked into these workflows that are awkward and um we want just the raw file. So that would be my thing is like they are modern too.  
   
 

### 00:23:31 {#00:23:31}

   
**David Olsson:** I did a search and since I use AI cursor, you know, coding um an MCP makes a lot of this stuff happen without having to do any coding. So there's either the ability to use some uh to write some code to download all the files to build that. So you can manually do it or you can use an MCP that then you can just prompt your way through it and then um you would um either download them to your desktop and then uh sync them or you would what we'll do is figure out a pipeline that will do it automatically. So that so the pipeline right now so no right now the pipeline I get a Google document that automatically gets generated from file fireflies I need to figure out the GitHub uh trigger for that I believe that  
**James Giroday:** Yeah, I was trying to figure out the pipeline, but I think I think it's going to cost money. Did you maybe would you maybe use like Zapier to do that?  
**David Olsson:** uh so that's how I would suggest somebody that doesn't um have uh like doesn't have the coding proficiency there's That's exactly what those tools are for, gluing these things together.  
   
 

### 00:24:43

   
**David Olsson:** So, you figured it out. So, you've got something in Zap in Fireflies. Does Zapier have a connector between that and GitHub? Like everything should connect to GitHub. Like Yeah.  
**James Giroday:** Well, even say like say you want the upload to happen like on the cloud like say I have a computer that I just don't want to save anything onto ever.  
**David Olsson:** Yeah. It's a smart thing. Yeah.  
**James Giroday:** Would you you would you still use Zap year if you like to run that process? like where would you run that API call and upload mode.  
**David Olsson:** So it so things need triggers and and that's where the integrations come in. So, Zapier can integrate with your meetings and then it would know when you've had one and saying that it could integrate with uh I don't  
**James Giroday:** He  
**David Olsson:** know to what degree um Fireflyy's API allows for triggering other other services. It's it it seems to be a restful. So, you have to determine that and if it's something you schedule, you schedule it or either that or it happens automatically.  
   
 

### 00:25:51 {#00:25:51}

   
**David Olsson:** And these are programmatic things and they're limited by how much you pay. Um, but you can certainly with Zapier or something like that, you can time things like you can you can certainly I'm sure you can connect it to your uh calendar so that every time you have a meeting, right  
**James Giroday:** Yeah.  
**David Olsson:** after your meeting, you go look for a new file, you know, like that's the kind of thing it's supposed to do. Um,  
**James Giroday:** So, so say we wanted to have Miles conduct the meeting then um he's got his own say we're going with uh Fathom and Zapier unless there's something cheaper and better. Um, but just just for example, obviously, so say Miles, say you're on vacation and Miles wants to conduct the meeting and upload the transcript to the GitHub that week. Does that work? Can he sign in with his own Fathom account and then it gets triggered through his Google Drive right up there?  
**David Olsson:** That's one way it could work. It's it's easier if it's say like one person sets up the meeting.  
   
 

### 00:26:57 {#00:26:57}

   
**David Olsson:** It's owned by that calendar event and that person owns the calendar event and then you have moderators inside that. And that for the reason for that is then you just have one account connected to that one zap year kind of thing connected to the to to to Fireflies instead of needing to have like federated identities working in an oath situation. The second thing I said is a nightmare.  
**James Giroday:** I know your your 8 amii.com idea of having like disperate groups somehow collaborating which is this what did you call it? Federated Yeah, I'm still fascinated by I'm like, is this possible?  
**David Olsson:** Oh, you're ident being able to have uh lots of people log in and do the same sort of thing, right? So, yeah. Um well, it's how you do most things, right? So, you want to be able to like if you have a platform, you want to be able to if it's team oriented, you have lots of teams and so you enable people to log in with whatever ID they have and what it does is it has a loop.  
   
 

### 00:27:56

   
**David Olsson:** You can verify their ID. the Googles, the whatever I call them, the federated identities like um but it's typically technically called OOTH and everybody hates it.  
**James Giroday:** It's called what? Holas  
**David Olsson:** There's just these there's just these protocols for authorizing people and they're very they add a layer of complexity on top of your application that doesn't allow for getting s\*\*\* done real quick. Um and that's kind of this mode that we're in. And so it would be easier if um if one person just scheduled a year's worth and then they had the Fireflies account or they had the Fathom account and then you would be able to see these things connecting with Zapier quite easily.  
**James Giroday:** Okay. Sorry. What's that concept again? Olaf. Au. Is that Oh, ooth.  
**David Olsson:** Ooth it's it's a Yeah.  
**James Giroday:** Yeah. Yeah. Yeah. Yeah. Yeah.  
**David Olsson:** Yeah. Yeah. And then he's got this other thing single SSO uh where you can log into a whole bunch of things with one address.  
   
 

### 00:28:51

   
**David Olsson:** So or you can have a whole bunch of addresses log into one account. So you can do these things that are uh wonderful or you can have no account and you do a login, right? That's the best one. You just quickly get an account. You just get an email verification.  
**James Giroday:** Okay.  
**David Olsson:** But no, so there's the what you're what you're doing is you're thinking about it systematically above what I've done as a simple solution path.  
**James Giroday:** Sorry. Sorry if that seemed like an interrogation. I I I was trying to think through something and Yeah.  
**David Olsson:** You're thinking, okay, any video thing, any meeting, any person, any transcript to GitHub and that's just a too many variables for the MVP.  
**James Giroday:** Yeah.  
**David Olsson:** Um eventually you can have that because you want to say like I just want to do this for myself and two other people. So you have your own version of that s\*\*\*. But in this case we have an organization that can run under the sponsorship of certain accounts instead instead of having a instead of having a system where you buy an account that does all that.  
   
 

### 00:29:49

   
**James Giroday:** Mhm. Mhm.  
**David Olsson:** And so Fathom is a good one for it's got a better interface, does better notes and stuff. I don't know it's transcript and API, but listening to the CEO, he's a he I like him. This is a while back when I studied him and but we had adopted this and I and I had tried multiple times to get on top of the number of transcripts we had, but the previous way of downloading them was just butchered, man. I can only do so many of it per day and that just didn't work very well. Um, and so now the idea is I'll get them all out and we can have a decision. We can have a level set and say we're we're up to date. We have two years of transcripts for a whole business. Um, it's quite wild. Um, and then for this for this room, this is number 51 with the same subject uh heading for the And so that's that's what stitches this together, right? the same subject in the email and the and the calendar event and then the reporting that that little tag allows me to draw down reports from Fireflies without any effort.  
   
 

### 00:31:06

   
**David Olsson:** Just putting that in the uh invites and in the calendar event. So there's no technology there. That's a protocol. That's a practice and it's just super light.  
**James Giroday:** Yeah, that's light. I like how light that is. It's just like Yeah.  
**David Olsson:** Yeah. Um and that's what kind of the whole paradigm I'm tried to adopt is like there's ways of working with these things in a lightweight manner. If you figure it out soon as you get into the federated identity stuff, then you're wanting to make money.  
**James Giroday:** Well, I don't know. Yeah.  
**David Olsson:** It's no it's no longer light foot is what I'm getting at. It's like um it's a little bit heavier, but that that  
**James Giroday:** I mean, if you I feel like you the I feel like the really the the thing that turns you into wanting to make money is when you're starting to have to pay for anything. If you're using stuff that's open source and it's just a tool for to share, then yeah, I mean that's good.  
   
 

### 00:32:07

   
**David Olsson:** Yeah, but what I mean is that if you're going to invest in making sure all that works really well, it's going to be there's going to be infrastructure underneath it. You got to make money to do that.  
**James Giroday:** Mhm. Yeah. If you're spending money, you got to take be taking money, too.  
**David Olsson:** Um, yeah. Yeah. So, I'm not like it's if this pattern works, it's a super good one to then open source and say it's just really easy to adopt. You just need to, you know, and the meta pattern is the one you've described is like you need to have meetings and they have to have videos and they got to have note takers. You got those things then you can do these other cool things. Um, and that's what we're trying to get the other cool things in place. And so I'm ready to now move on this um, autocratically. How's that? Uh, decision is decision m decision is momentum instead of uh, anything else.  
**James Giroday:** go for it.  
   
 

### 00:32:58

   
**David Olsson:** So your structure that you were talking about before startup empathy is enough. Um, so I'll get that going. Um, it looks like it did it.  
**Myles Holt:** where you running  
**David Olsson:** Um, well, it connected the MCP and now it's asking me for my key. And then it says it will put it in a directory in directories named after the date of the meetings. And so I think it's ready to go, but I'm very doubtful. So the Firefire stuff is is the API was really flaky. And so I'm like until I can see it do a whole bunch of different things. That's why I would like to get out of it and do a reset in terms of the environment is different for analyzing these things, right? So I would look at any new vendor saying how can I vibe code like how can I prompt my database of transcripts  
**James Giroday:** Can I c can I pause and I I I want to more fully understand this, but I want to make it easy on you.  
   
 

### 00:34:01 {#00:34:01}

   
**James Giroday:** I don't want to pepper you with questions. So, let me try to explain what I think you're doing right now, which is, okay, we've got a Google Meet calendar invite. And each time we have one of these, we show up. Fireflies also shows up. Once the meeting's over, you make an API call to Fireflies to download the transcript and then you use cursor and claude code to uh add that into the context of an MCP. Do you can you clarify that one?  
**David Olsson:** Um, no I would use so the MCP helps with the transport of things from from Fireflies to either the desktop or to a server. And say I'm doing it manually. You've got it right. I would be on my in cursor. I would be prompting this. I say download last week's um uh 8 a.m. transcript and audio file. It would do that. It would go into the directory appropriately named and I can I can show you. Well, just as a point of reference, you can see over here um put your API key and it'll it'll put them in here.  
   
 

### 00:35:29

   
**David Olsson:** And then I could do any number of things. Um because that would I would make a repo. I would make the 8 a.m. AI directory a repo and then anytime things are added to the repo um I could have watchers on it and the watchers would then add a commit and then I could manually or  
**James Giroday:** Yeah.  
**David Olsson:** automatically push it to to the account.  
**James Giroday:** This is cursor that you're in.  
**David Olsson:** So this is cursor right now. And so I had some difficulty. It was like it was it started building me a downloader. I'm like I'm just supposed to be able to ask you to do this. And so I'm like okay it's not installed. And so I had to go through this process but it is it's telling me it's installed right now. So this stuff over here is one. So here's here is a complete table of all of the meetings all 50\. The last one was all relation uh AI relationship coding assistance cognitive debt. Um Graeme explored influence organized transcripts for analysis.  
   
 

### 00:36:42

   
**David Olsson:** That's that's what I'm trying to get going. So, um, use Fireflies to list all the ADA meetings for yada yada yada. And so, I I put it in. It says I did put it in, but that's where I'm at with that. Um, and so that what it'll do is this is me manually downloading them into the directory. And then the directory is has an associate.  
**James Giroday:** Yeah.  
**David Olsson:** It is it is the repo and it will and I will manage that or yeah it's the same repo.  
**James Giroday:** Yeah. Wait. So there So there is a repo on GitHub for this.  
**David Olsson:** Um I am remote and it is origin and I'm going to push to origin and then because I own it and all that there's going to be a a few less steps than normally but that's how that would  
**James Giroday:** Yeah.  
**David Olsson:** work. But most likely I would do that for maybe a week or two. This is a just this is how programmers go. I would do that for a week or two because then I would either get lazy or forget and then I would step back and say okay the steps are straightforward.  
   
 

### 00:37:47 {#00:37:47}

   
**David Olsson:** I can take myself out of them and then it would put them on a server that would either do the cron jobs get triggers um be pulled like it would be an endpoint and then could be triggered. we would figure out what that is, but it would instead of be instead of coming to me on my machine as an intermediary step and managing that, it would just go make a call and then it would do something and then go bang right into GitHub or get routed or yeah, it would be most likely netifi or something on AWS depending on how much server it requires.  
**James Giroday:** on a you said on a server somewhere. Yeah.  
**David Olsson:** it's most likely just just a call like an endpoint and then and then the endpoint helps make that happen. Um so there's and I'm you know I'm talking out of my hat because these are conditional things and there's lots of ways of doing them now. And so that's the neat thing is like what you tried to do with Fathom and and Zapier as the as the technology set provided a path there.  
   
 

### 00:38:50 {#00:38:50}

   
**David Olsson:** You just have to make different assumptions. But if you make the same assumptions all the way along like conventions like call things the same thing in your calendar and then um then then that gets tracked into your transcript naming and then that gets you know then eventually makes it into your GitHub repo is the same sort of thing. So, it gets organized according to a really essential tag. And since we meet at 8 a.m., you know, the the um that's there's a time and a date. Um and then, you know, if we got really organized, then we would have all the metadata around the system that says who attended and all the other things. Um,  
**James Giroday:** Miles, Miles, what are you thinking? Is this the  
**Myles Holt:** Well, I'm curious. Is this just an experiment? Like I I totally understand what you're trying to do. um is was it just an experiment to get an MTP to um basically parse out the transcripts and then get it into a shared space or are you working on some sort of business case?  
   
 

### 00:39:52 {#00:39:52}

   
**Myles Holt:** Um just cur about curious about the motivation What happened?  
**David Olsson:** so there's there's a piece of string there, right? So this peer group, the way that it works, the way that meetings work, the things left on the table, once they're in the repo, you can have multiple agents going at it. Call them the curiosity council. They're going at it looking for things inside one meeting. You know, this this group actually personas from this group. It' be great. Coming at it from different points of view and then saying this meeting does this. What about all the meetings? Oh, guess what? There's a thread going through it. And that's the power that I see in these agents is like will you do something really primary like have these conversations and then have these agents try to stitch the pattern recognition together for you or ek out questions that are really good and that can happen at a secondary level. And that's kind of this pattern that I'm currently working to try to see if we can support ourselves better saying do the work.  
   
 

### 00:40:43 {#00:40:43}

   
**Myles Holt:** I see.  
**David Olsson:** It's kind of like quality control, right? But it's actually like in knowledge mining or something. Um, and but it's a it's a it's a it's an a tertiary piece to your core effort. Like this is the most intelligent engagement we will have is in these rooms. Um, we're only capturing the words right now, but after this it's just information and so yeah.  
**James Giroday:** Yeah, I kind of see it. Sorry, dude. Are you can I?  
**David Olsson:** Okay.  
**James Giroday:** So, uh yeah, I kind of just see it as like a resource as well for curiosity of everybody. So, if you can find a really good preferably free way to make uh the conversations accessible for knowledge mining, just like you said, then that's like a really powerful thing. It's a really powerful foundation for work later to like look back on that stuff and synthesize it or mine it for ideas or workflows. It's like what did he say about this? How does that work? It's like this whole thread to continue to pull on.  
   
 

### 00:41:57 {#00:41:57}

   
**Myles Holt:** Yeah, I do see the value there as well. What's in what I'm thinking about would be interesting is um because you could have a secondary pass on all over the over all the topics and have the Asians sort of spawn off and do some curiosity exploration there. But how do you come back and then now summarize the results of that and then like what's the feedback loop? You know what I mean? So for next meeting maybe we talk about these other this other layer that's come back and said yeah um we realize that there's you know you had 10 things and now we have a thousand. Um, what does that look like in terms of structure? You know,  
**James Giroday:** I mean, I think for me, for me, the takeaway is like once you have that substrate, as David put it, and you start mining it for curiosity and that stuff, I feel like that the what you're acrewing there  
**David Olsson:** very very good.  
**James Giroday:** is just the a whole understanding about how to mine this activity and it kind of goes towards understanding things like change management.  
   
 

### 00:43:03

   
**James Giroday:** So, if I'm just doing my job and I do a bad kind of a bad job of like implementing a new tool and I go like, oh, like I didn't even know change management exists, you know, before I'm just like operating at layer level one. I'll call it level one, not to get confused with blockchain here. Level one, not layer one. Um, you know, once you have that foundation of the accessible transcripts for every mine, now you're working at level two, you're like, "Okay, well, now I know how to, you know, kind of sick these agents on this transcript and and get get, you know, find some curiosity." And then maybe there's other levels, too. Like, I don't know. But that's where I want to be. I want to be at level two.  
**Myles Holt:** Well, it could be like it could be infinite uh really depending on uh the topic we're talking about, right?  
**David Olsson:** Mhm.  
**Myles Holt:** Because at some point it's going to get into a philosophical discussion. Um and then  
   
 

### 00:44:03 {#00:44:03}

   
**James Giroday:** Yeah. Yeah. Yeah. For sure.  
**David Olsson:** So other other example of the pattern um exactly the way that you're kind of lading it up is that I have all these repos move quickly. They they certainly serve a purpose. I've learned something and I can carry that forward as a corpus. What does it mean? And what have I left on the table? I've wondered that. I wondered that with work sona. I did that with work sona twice. readme's technical specs then bit you know sending business agent at it marketing agent and having the same reports done over each of them that was so one readme technical spec next one analyze it for themes and where it can go and direction and opportunities and then the next one consolidate those and provide me a story about it and it told the work zona story to me better than I've ever heard it and it provided me new language around the fact that it was consistent and there was pathways through it and it identified the themes but I had to work at this building block level.  
   
 

### 00:45:12 {#00:45:12}

   
**David Olsson:** You started with this one thing. I had these things. Document themselves as you normally would. Then point some agents to understand it in the context of business or whatever. Then get them to relate to each other and then build a narrative over top of it. And so you have to build those building blocks to get to that narrative. I didn't know what that was. I wanted the text back and the read me and I figured I could summarize those somehow. And then what it did allow to do is say here was the direction now where can we take it given we're talking to these five people.  
**Myles Holt:** Yeah. like was the theme that came that came out of it was it basically your business model right?  
**David Olsson:** Uh it was the it was the principles that drove the business model. The the principles and the values that would make anything happen regardless of the opportunity and the pathf finding. You know what I mean? Like the strategies and they're just stupid simple things.  
   
 

### 00:46:04 {#00:46:04}

   
**Myles Holt:** Yep.  
**David Olsson:** So what you can do once you have that corpus is you can then was this here traces of this can you do this and you can do that with it if you've got it structured well enough and but that's that's that's something I think you pointed to and I think you both what does it look like well it's all human readable at this point for me the readmes are good they make the app stand on its own the technical spec allows me to say there might be synergies with the next ones above that again I Just have agents doing it.  
**James Giroday:** Does that Oh, Miles, does that sort of speak to the motivation thing?  
**David Olsson:** No.  
**James Giroday:** Does that sort of answer that or are there still questions that you have probably about that?  
**Myles Holt:** Um yeah, like I I don't understand the space in terms of like I understand this meeting is a collaborative effort for ideas. Um but at some point we we need a paycheck. So um you know it's it's I I always go back to like what business problem are we trying to solve here?  
   
 

### 00:47:11 {#00:47:11}

   
**Myles Holt:** Um  
**David Olsson:** So, so if we have a a project and we do the same sort of thing with a project and we use this meeting room is this is the core sort of backbone to how we manage the project and we discuss things here in the project. We can, this is one of the first views of this, is we cue things up well and say say things that are keywords, then we can get prompts based on them and we can be self-reerential in our meetings and get the prompts to be acting on what we're doing. This is a step back from that, saying do the work in your project and have everything about project management happen on as triggers to what you discuss. So the path to project management in my company isn't hiring a project manager. It's figuring out h how to have that as a as a wing to the core activities and this pattern of we are having meetings. How do we make that structural for us moving forward? Because right now doing the forensic effort moving backwards to see what the structure looks like.  
   
 

### 00:48:09 {#00:48:09}

   
**James Giroday:** I I can speak to I can speak to that a little bit, Miles. I feel like I Yeah. Like I've kind of shown up with just uh mostly like patience and just like general directionless interest, which is kind of how I showed up, which is kind of how I met David. But anyways, without getting into that um like what is the like so I might say yeah like the answer to your question what is the motivation for my showing up here in some ways definitely continues to be like what am I personally acrewing and I think what I'm hoping to acrue maybe is like this whole idea about understanding change management better and understanding how to um action agents better because even if I don't get paid for showing up here, like though that's a skill that's incredibly marketable and is probably going to be super useful and like if I know how to do that, I'm going to be fairly far ahead of the curve or at least the front part of the curve, you know?  
**Myles Holt:** Yeah. So, if I can interject just there, the question wasn't the motivation for showing up to this meeting.  
   
 

### 00:49:28

   
**James Giroday:** Yeah.  
**Myles Holt:** It was just the motivation for um the activity of parsing the transcripts. Um, I was just curious if that was just a little, you know, can we do this? Let's see how we do it or if there was a larger business case for doing that. I mean, I think like I'm here to learn as well and and my motivation is just continued growth. So, um, I wasn't really questioning that. It was just the specific topic of getting the fireflies transcript par.  
**James Giroday:** Sorry, we took took the question too meta.  
**Myles Holt:** Yeah. Okay.  
**David Olsson:** But the the project itself is one of being able to say we have this this asset that's just sitting there and to surface something in We've had some really wild conversations, man. And even if we just if we just figured out how to um build a wiki of some of the better transcripts and and then just every now and then publish it on X, that's something, you know, and and  
**Myles Holt:** I see. Yep.  
   
 

### 00:50:26 {#00:50:26}

   
**David Olsson:** so that's a minimum requirement is is is showing the value beyond ourselves. But one just showing to to to um James's point like I'm excited and I'm not sure what we we'll uncover, but if we do go back and point the right agents at it, I know themes surface and um a lot of it is about what you just said is James is like there's something that is sticking with you and there's a motivation to have more of it. Um how about wouldn't it be neat to uncover intuition? It usually does have a backwards set of footprints and then to be able to recognize it more readily in the moment because um I do believe this is the future of work. This is and this is this is the only time in my week where we're talking about things that don't have to make money but have probably have the most impact in terms of positioning ourselves better to do that.  
**Myles Holt:** Yeah.  
**David Olsson:** Um I don't something.  
**Myles Holt:** Yeah. So, you're going to you're going to eventually continue to roll with this idea of of taking the transcript and and putting it into GitHub repo and then possibly publishing it.  
   
 

### 00:51:35 {#00:51:35}

   
**David Olsson:** Yeah, we'll talk about that. I'll make this happen and we'll talk about the next level of things that how that can occur. Um, and then my hope would be that people have access to you can just go down and copy and paste things into anything you want. But, um, we can programmatically do things just like Fireflies does. It it, you know, sends out a summary of things. And um I just know that if we go backwards in time, we would have some pretty big pretty interesting questions to ask of each meeting. Um and then that would be like, well, you guys talked about that when So how about how about this? Every past meeting is a unit text for the current meeting. How's that?  
**Myles Holt:** That's well yeah that's what I was saying like what's the feedback loop um of the second layer. Yeah.  
**David Olsson:** Yeah. So I don't know. How about that? I I'll try to really picture that that that that each of them is a unit test.  
   
 

### 00:52:25 {#00:52:25}

   
**James Giroday:** Can I ask a question while we still have a bit of time? Um, there was maybe I feel like there's been some interest around having a demo. Uh, as I mentioned before, demos would be best if they have a bit of lead time. And it's I mean, even if it's not a demo, um, here I want to do a bit of an experiment. So, I'm going to call for a vote here. All right. And you can show zero to five uh, fingers. Uh, one is you oppose it pretty strongly. Two is you're slightly opposed. Three is your neutral. Four is you're in favor, but like not strongly in favor. And five is you're strongly in favor. So, oh, we've got another visual participant here.  
**David Olsson:** Nice one. She's got a vote.  
**James Giroday:** Oh, here for them.  
**Jen Boger:** Yeah. No, I've I've been listening the whole time. I'm just sitting listening because it's a good conversation and I just want to see where it goes.  
   
 

### 00:53:27 {#00:53:27}

   
**Jen Boger:** So, but I've been listening.  
**James Giroday:** Well, you're you're welcome to to throw in a vote as well.  
**Jen Boger:** Okay.  
**James Giroday:** So, what do you guys say we um reserve 20 minutes for somebody to claim? I'll just like email the group and say like next week, does anybody want to present something for 20 minutes? 10 minutes of presentation, 10 minutes of um question Q\&A and uh out of zero to five, if that's okay, who who's in favor of this?  
**David Olsson:** Yeah.  
**James Giroday:** I in in my own idea, I'm about a four. I feel like that's a pretty good idea.  
**Myles Holt:** Yeah. I mean, I'm a five. I mean, there's no harm in asking people to present if there's not if if if um there's takers, right? And if there's not takers, then we just continue with the Yeah.  
**David Olsson:** Yeah.  
**James Giroday:** Yeah, totally definitely an option to pass and I'll I'll make that clear.  
**David Olsson:** Um I think what I would like to to make it easy for some people too is like they're using tools, right?  
   
 

### 00:54:22 {#00:54:22}

   
**David Olsson:** And so here's a demonstration of how screwed I am. Um Scott brought brought a couple of those to the meeting and they were great like and then he walked away with solutions, man. So, um, you know, presentation of some sort, demonstration, people come up with little tricks like like seriously the the naming convention thing.  
**James Giroday:** Amazing.  
**David Olsson:** Learned that one like 30 years ago in my career because I had to because there wasn't a lot of version control. Turns out still works in nason technology everywhere. So that's a the like inside inside the curs the tools that we have like um cursor you're writing little rules like that like tiny little rules and that's how you get ahead. So I give it five you send out an email is what I also heard. So that was why all five fingers went up.  
**James Giroday:** I yeah, I committed to it. So, I will do that. Although, I just realized I won't actually be here next week, but I'll still send the email. I'll send it today.  
   
 

### 00:55:20

   
**James Giroday:** It'll give people a lot of time to claim it. Yeah, I'm on vacation next week. I'm in Ontario.  
**David Olsson:** Oh, Jen.  
**James Giroday:** Jen, are you in Ontario right now?  
**David Olsson:** She is.  
**Jen Boger:** I am in Ontario. I'm at my in-laws cottage actually. That's why I'm outside and it's very hot. There's no air conditioning here. So, last night it rained.  
**David Olsson:** It looks hard.  
**Jen Boger:** It's crazy. They stole all our heat. It's like been a drought up here and super hot. All the lawns are brown and it's like, oh, Colona got all the cold rainy this this summer and they got all the hot heat. So, yeah. Yeah, we're part If if Air Canada doesn't go on strike.  
**David Olsson:** Well, that's what you got to look forward to, James. There you go.  
**James Giroday:** Yes, absolutely.  
**Jen Boger:** Hey, are you have you seen that?  
**James Giroday:** Yeah, they uh we we had our Canada flights and we actually bought WestJet flights as well just to cover our Yeah.  
   
 

### 00:56:09 {#00:56:09}

   
**Jen Boger:** Just uh cover your cover your bet. I like this idea a lot and you know kind of just throwing my last few cents in on the idea David's got. I think it's, you know, goes beyond just I mean, one thing you can do is parse past calls, but especially if they're with specific groups, right, to extract themes. But the beautiful thing is with the agents, it's just like such a wealth of knowledge that you can keep going back to and then have a different persona so that as things arise where you're like, "Oh, here's a use case maybe. Well, is there information there?" You can just keep going back to this like and it could be a client too a client. It can be a group like this.  
**David Olsson:** Mhm.  
**Jen Boger:** You can you can take it all and just like organize it. I think an interesting thing that I'm wondering is can we start throwing labels on our calls beyond just the title, right? So that you can start binning things after a call.  
   
 

### 00:57:14 {#00:57:14}

   
**David Olsson:** So so that would be that would be that would be the secondary sort of processing I think we could do is tagging the crap out of things quite easily. Um and so to keep the flow until we break it, I would suggest that.  
**Jen Boger:** Yeah.  
**David Olsson:** But yeah, adding a dash and then something after the dash in terms of parsible protocols certainly makes yeah and for advertising purposes too.  
**Jen Boger:** Right? Because like you you might have discussions like this that may also be related to a certain project somewhere else. And so you want both labels on there.  
**David Olsson:** people see the thread in their emails, the subject line, it's it it can help people make decisions about their time better, too. So, I think that's a that's a good thing to advance to and to consider when I'm doing this next little thing. But, um, yeah, I'm I'm curious. I had to do this kind of thing for healthcare when I was doing the interviews um because I had to get transcripts and I so I used Fireflies to create transcripts and then it had some lightweight agent stuff in it but it was the ability to look at five transcripts at once and say build me a persona and I'm like man you just saved me 20 hours of work like literally 20 hours of work I couldn't use it though it was crap it was 35 I couldn't use it But um now I kid now nobody wants a persona though.  
**Jen Boger:** a good start.  
**David Olsson:** That was so funny.  
**Jen Boger:** And you've inspired me to label my meetings more sensibly with some  
**David Olsson:** Yeah. Um documentation, lightweight documentation goes a long way.  
**James Giroday:** Yeah.  
**David Olsson:** So yeah, we'll leave labels on the table for next time. Well,  
**Jen Boger:** Like I say, top topic for next meeting that you're at.  
   
 

### Transcription ended after 01:01:07

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*