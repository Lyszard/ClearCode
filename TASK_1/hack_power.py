#HACK CALCULATOR



def hack_calculator(hack = "baaca",letters = {'a':1, 'b':2, 'c':3},phrases = {'ba':10, 'baa':20}):
    power = 0
    temp = 0
    phrases_copy = phrases.copy()
    overlap_vars = []


##################################################################
    #----calculating power only from letters----#
    for key in letters.keys():
        n = hack.count(key)

        for i in range(1,n+1):
            temp += i * letters.get(key,0)


        power +=temp
        temp = 0
    print "power from letters:"
    print power



###################################################################
    # ----finding the position of the phrase in the hack and assigning it as value to a copy of the phrases----#

    for key in phrases.keys():
        start = hack.find(key)
        end = start + len(key)-1
        temp_list = [start,end]
        phrases_copy[key] = temp_list

        print "phrases_copy:"
        print phrases_copy
####################################################################
    # ----checking the position of each phrase with all the other phrases to find overlappings----#

    for phrase in phrases_copy:


        for phrase2 in phrases_copy:
            if phrase == phrase2:
                pass #dont check with yourself
            else:
                # ---checing which phrase should be added to the power ----#

                if phrases_copy.get(phrase,0)[0]>= 0 and phrases_copy.get(phrase2,0)[0] >= 0:

                    # ----finding shared "area"----#
                    beg = max(phrases_copy.get(phrase,0)[0],phrases_copy.get(phrase2,0)[0])

                    end = min(phrases_copy.get(phrase,0)[1],phrases_copy.get(phrase2,0)[1])
                    print "beginning:"
                    print beg
                    print "end:"
                    print end
                    shared = end - beg
                    print "shared"
                    print shared

                    overlap_temp = [beg,end,shared]

                    if len(overlap_vars)==0:
                        overlap_vars.append(overlap_temp)
                        # ----if shared value is more than or equal zero it means the phrases are overlapping----#
                        # ----To resolve the conflict I choose the longer word after the substraction of the shared area----#
                        if shared >= 0:
                            if len(phrase)-shared > len(phrase2)-shared:
                                power += phrases.get(phrase,0)

                            else:

                                power += phrases.get(phrase2, 0)
                        else:
                            # ----if shared is less than zero it means that phrases are not overlapping----#
                            power += phrases.get(phrase,0)+phrases.get(phrase2,0)

                    else:
                        # ----To prevent checking same phrases twice eg phrase number one with number two and number two with number one----#
                        # ----I just check if the same values happened in the past----#
                        for vars in overlap_vars:
                            if beg == vars[0] or end == vars[1] or shared == vars[2]:
                                pass

                elif phrases_copy.get(phrase,0)[0] >= 0 and phrases_copy.get(phrase2,0)[0] < 0:
                    power += phrases.get(phrase, 0)

                elif  phrases_copy.get(phrase,0)[0] < 0 and phrases_copy.get(phrase2,0)[0] >= 0:
                    power += phrases.get(phrase2, 0)

                else:
                    pass

    print "POWER"
    print power
    return power


hack_calculator()





