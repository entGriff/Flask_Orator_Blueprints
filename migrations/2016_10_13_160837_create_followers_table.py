from orator.migrations import Migration


class CreateFollowersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('followers') as table:
            table.increments('id')
            table.integer('follower_id').unsigned()
            table.integer('followed_id').unsigned()
            table.timestamps()

            table.foreign('follower_id').references('id').on('users').on_delete('cascade')
            table.foreign('followed_id').references('id').on('users').on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('followers')
