from orator.migrations import Migration


class CreateMessagesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('messages') as table:
            table.increments('id')
            table.text('content')
            table.integer('user_id').unsigned()
            table.timestamps()

            table.foreign('user_id').references('id').on('users').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('messages')
