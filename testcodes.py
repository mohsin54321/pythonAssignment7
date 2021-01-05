AllVar = ['Intro','NameOfMyFavoriteSong','PublishedYear','Artist','Conti1','Conti2','DurationInSec','Conti3','Conti4','Genre','WhereYouCanEnjoy']
EachVarValue = ['My song of choice is : ','Beautiful Sunday', 1972 , 'Daniel Boone','Although this song is quite old for now, listening to this song is quite recommended.','It takes around','188','seconds.','Genre :','Rock.','You can find this song in YouTube, Spotify, Joox and any other applications that fuctions to play music.']
songdictionary = {}
counterforlist2 = 0

for a in AllVar:
    songdictionary[a] = EachVarValue[counterforlist2]
    counterforlist2 += 1

print('Hello, Welcome!')

for b in AllVar:
    if b == AllVar[1:4]:
        print('Do you want to guess what is the', AllVar[b] + '?')
        reply = str(input('Yes or No? 5 chances for each questions. Type right down here\n'))
        if reply == 'Yes' or reply == 'yes':
            for c in range(1,6):
                answer = str(input('Chance {} / Your answer: '.format(c)))
                if answer == EachVarValue[1] or answer == EachVarValue[2] or answer == EachVarValue[3]:
                    print('Correct!')
                elif c == 5:
                    print('The answer is:',EachVarValue[b])
                else:
                    print('Incorrect answer.')
        elif reply == 'No' or reply == 'no':
            print(AllVar[0:b+1])
        else:
            reply2 = str(input('Skip all?\n'))
            if reply2 == 'skip all' or reply2 == 'Skip all':
                print(songdictionary)
                #Until here the code is working absolutely fine
    else:
        print(EachVarValue[0:b])
print(songdictionary)
