import journal
import os


print("------------------------------")
print("       JOURNAL APP")
print("-----------------------------")


print('What do you want to do with your journal?')
cmd = None
journal_name = 'default'
journal_data = journal.load(journal_name) #[] #empty list

    while cmd != 'x':
        cmd = input('[L]ist entries,[A]dd an entry, E[x]it')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)

        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd !='x':
            print("Sorry, we don't understand '{}',".format(cmd))

    print("done, goodbye")
    journal.save(journal_data, journal_name)
def list_entries(data):
    print('your journal entry:')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1,entry)) #with tuples

def add_entry(data):
    text = input('Type your entry, <enter> to exit') #list
    journal.add_entry(text, data)
    #data.append(text)

def load(name):
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data

def save(name, journal_data):
    filename = get_full_pathname(name)
    print('.............saving to: {}'.format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')

def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'Journals' + name + '.jrl'))
    return filename

def add_entry(text, journal_data):
    journal_data.append(text)
