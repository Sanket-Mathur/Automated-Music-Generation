# Automated-Music-Generation

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)

Listening to new songs has always been a great way to pass time or accompany some tasks in order to reduce fatigue and stress. Selecting new and personalized music to listen to is a mentally challenging and time taking task.

*To solve this problem, here is a project*

The project is built using Python 3, along with the Tensorflow and Keras modules to implement deep learning. An iPython Notebook was used to experiment and train the model using data from the following singers: 'Justin Bieber', 'Bruno Mars', 'Drake', 'Rihanna' and 'Adele'.

## Requirements

- Python
- Python Modules
  - Tensorflow
  - Keras
  - Numpy

## Steps to Run the Project

- Ensure python3 installation in the environment
- Ensure python-pip installation 
- Execute the command to install required python modules
  ```
  pip install -r requirements.txt
  ```
- Execute the script to generate songs
  ```
  python main.py
  
  # OR Optionally provide a file location to save the generated song
  python main.py > output_file_name.txt
  ```

## Issues

- [ ] Cuss words are not removed from the generated song
- [ ] Not all words are meaningful

## Example Outputs

Generation 1
```
ease remember me once more
When will I see it all
If this is a lit, I can't stand and come along be sometimes
I will fight like some here (Versan de without you And you got it go to me
fait (yeah)
Tritwe betiy (last when the sturs, muct it bettee
And I've got that I can try
It's with these botterra,, baby
Cause it here and don't think now I can't do 'til it's easth my life
Yeah
Do I let my love it
Surving My exples on you?
Where I hate the real nothin' all that was in the night, shoulder comp one
No telling me can Loak dowa with me
Till you word
Can go that trip in the way it hust
Our thing we can't be a waste, we might be alright
Sey, fuck a ofentions
All here youngling
uh I'm not enought
In everyday, yeah
if that let your face I know when I'm the life you're my eye with the night
There a on this chand
And the last that I let me be waiting on the day
And don't get is it the club going up to my srewargh
The ciss even breaket us here thing there
I don't want you back (uh)
You scooling befies away in the cluh?s
With it out of 
```

Generation 2
```
ck
When I go runnin', runnin'
Tryin' to graving you if it ain't no,
You ain't take my where you knew, shines, really what they got
In they don't rechird when She gonna have me
But I see your heart believe in mind
Oh, than a girl wish you got our losing Oh yeah Love 'em like te money I need you Bight eah
I just fight right betin' wasting up to stop when, you sceep this still, yeah
Now I'm fuckin' word
right I'm just keep this
I can't live it to relofe oh
Man book of these never like it
You slip like a dispailones
last night best having fuckoching call, ain't gone?
Yeah you feel me tonight, yeah, yeah
Feel only one
Oh, whoa
Oh you you both someone give me right?
But everybody now like a briggar thing
And no time, the music up away
Is when you're getting it
And I 
would call my life,
I came between 'Cause I will has through the world, but we'll be there so he and to my mone
Still that I never scaces of me
My end things gonna be aure the flack with me
But you're love in somebody to you, uher you give me love, yeah
Who wone to th
```

## Conslusion

There is a lot of room for improvement of this project in order to make the generated song more meaningful.

The deep learning model recognized basic grammar rules like capitalization and use of helping verbs along with sentence breaking and word formation. The vocabulary is not perfect in terms of English but the model learns how to use vowels and consonants in words in order to make them pronounceable.
