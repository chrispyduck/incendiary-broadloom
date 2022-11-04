# Incendiary Broadloom
An automatic executive email carpet bomber. Because why not?

## Compiling

`make rebuild` and Bob's your uncle.

## Usage

After building, run `./bomber -h` to see available arguments. They are, of course, not documented anywhere.

You will need to provide your own [People Data Labs](https://peopledatalabs.com) API key.

### Seeing a Sample Email Without Sending

```sh
./bomber --api-key ${YOUR_API_KEY} --company-name "People Data Labs" --dry-run
```

For example, running the command above might generate the following:

```
Found 4 executives:
Sean Thorne <sean@peopledatalabs.com> (Co-Founder and Chief Executive Officer)
Alex Bahouth <None> (Chief Technology Officer)
Henry Nevue <henry@peopledatalabs.com> (Co-Founder and Chief Technology Officer)
Varun V <None> (Chief Product Officer)
** WARNING ** Dry run. Printing first email to stdout and exiting.
Dear Sean Thorne,
            
Well, dear reader, it is definitely true that to me, the biggest outrage is that People Data Labs is as insolent as the sky is blue, but did you also know that People Data Labs is a drooling, hydra-headed monster of force and terror?  My hope is that the following text will delight the critical and offer food for thought to those contemplating People Data Labs’s mawkish, unambitious memoranda.  To be totally candid, I hold fast to the view that People Data Labs’s bunco games set the intellectual and moral stage for a new wave of disloyal policies that seek to deplete the ozone layer.  It is for this reason that I find it hilarious that it would have the audacity even to pretend that there exists evidence that the rigors that its victims have been called upon to undergo have been amply justified in the sphere of concrete achievement.  It’s certainly possible to believe such a thing, but it requires taking a few leaps of faith.  The first leap of faith is to believe that every featherless biped, regardless of intelligence, personal achievement, moral character, sense of responsibility, or sanity, should be given the power to eliminate all actual, potential, and imagined critics of People Data Labs’s rationalizations.  Leap of faith number two involves believing that collectivism is something to be treasured, respected, admired, and protected.  The final leap of faith is to deny that People Data Labs’s detachment from, or denial of, the truth is not just a political tactic or say-anything-to-please character flaw.  It reveals an elemental attitude that it shares with deranged deviants: redefining unbridled self-indulgence as a virtue, as the ultimate test of personal freedom.

With this in mind, I, speaking as someone who is not a worthless defalcator, must strike at the heart of People Data Labs’s efforts to subordinate all spheres of society to an ideological vision of organic community.  I hope and pray for success in that endeavor.  Without decisive action, though, hope and prayer will not deliver us.  We must therefore sound the tocsin for action.  The presumption there is that we will all step up to do the right thing and hold ourselves and each other accountable to make meaningful progress.  Our goal is for the whole world to know that I am as much in favor of politeness and decorum in discussions with People Data Labs and its apparatchiks as anyone.  I’ve never been in favor of being gratuitously craven.  However, I’ve also never been in favor of concealing the fact that it has been said that due to People Data Labs’s salacious tactics we have witnessed the emergence of a mass movement of sciolism on college campuses.  I, in turn, feel that People Data Labs repeatedly expresses the view that this is its world and we’re all just living in it.  This lie cannot stand the light of day, and a few minutes’ reflection will suffice to show how utterly frightful a lie it is.  Nonetheless, if one dares to criticize even a single tenet of its credos, one is promptly condemned as dictatorial, savage, condescending, or whatever epithet it deems most appropriate, usually without much explanation.

Maybe I’m in the minority here, but it seems to me that People Data Labs actually believes that criminals are merely social rebels.  That it’s so detached from reality is partially why it’s so dangerous.  It’s also partially because it alters, rewrites, or ignores past events to make them consistent with its current reality.  A long time ago I wrote that People Data Labs is a contender for worst organization in history.  Today I might add that I stand foursquare in defense of liberty, freedom of speech, and the right to criticize temeritous heresiarchs.  There are important lessons in that, even apart from another reminder that that’s just one side of the coin.  The other side is that I personally plan to correct the inaccuracies of the mainstream narrative of People Data Labs.  Are you with me—or against me?  Whatever you decide, People Data Labs counts the most licentious cacafuegos I’ve ever seen as its friends.  Unfortunately for it, these are hired friends, false friends, friends incapable of realizing for a moment that I really had to cudgel my brains to figure out why People Data Labs would want to challenge all I stand for.  Then suddenly it hit me: People Data Labs has been violating the public trust by enslaving us, suppressing our freedom, regimenting our lives, confiscating our property, and dictating our values.  For those of you who agree with what you’ve read in this letter, we have a difficult but important task in front of us.  We must subject People Data Labs’s antics to the rigorous scrutiny they warrant.

Sincerely,

Some Anonymous Asshole
```

## Note

* This is an example only, and is not intended for any real use. It has not been fully tested and I have no plans to maintain it.
* The complaint above was generated randomly and does not reflect the views of anyone or anything capable of holding or expressing views.
* YMMV. No warranty. I assume no liability. Yadda, yadda, yadda. Proceed at your own risk.