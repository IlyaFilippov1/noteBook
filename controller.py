import note

atr_of_note = {'id': '',
               'Added': '',
               'Title': '',
               'Body': ''}

list_of_notes = []

def view():
    print('Commands:\n'
          '   add - add note,\n'
          '   list - view all notes,\n'
          '   edit - edit note, \n'
          '   delete - delete note, \n'
          '   exit')
    while True:
        choose = input('Please enter the command: ')
        if choose == 'add':
            title = input('Please enter the title: ')
            body = input('Please enter the message: ')
            object_note = note.Note(title, body)
            list_of_notes.append(dict(zip(atr_of_note, [object_note.get_id(),
                                                        str(object_note.get_create_date()),
                                                        object_note.get_title(),
                                                        object_note.get_text()])))
        elif choose == 'delete':
            note_id = input('Please enter the id of note: ')
            for your_note in list_of_notes:
                if your_note['id'] == int(note_id):
                    list_of_notes.remove(your_note)
                    print('Your note was remove ( id_note =', note_id, ')')
            for your_note in list_of_notes:
                print(your_note)
        elif choose == 'edit':
            note_id = input('Please enter the id of note: ')
            for your_note in list_of_notes:
                if your_note['id'] == int(note_id):
                    your_note['Body'] = input('Please enter new message: ')
                    print('Your note was edited\n', your_note)
        elif choose == 'list':
            for your_note in list_of_notes:
                print(your_note)
        elif choose == 'exit':
            print('SEE YOU LATER!')
            break
        else:
            print('Your input is incorrect')