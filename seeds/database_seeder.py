from orator.seeds import Seeder
from .users_table_seeder import UsersTableSeeder
from .messages_table_seeder import MessagesTableSeeder
from .followers_table_seeder import FollowersTableSeeder


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(UsersTableSeeder)
        self.call(MessagesTableSeeder)
        self.call(FollowersTableSeeder)

