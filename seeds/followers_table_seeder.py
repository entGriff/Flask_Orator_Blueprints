from orator.seeds import Seeder


class FollowersTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        with self.db.transaction():
            twittor = self.db.table('users').where('name', 'twittor').first()
            john = self.db.table('users').where('name', 'john').first()
            jane = self.db.table('users').where('name', 'jane').first()

            self.db.table('followers').insert([
                {'follower_id': twittor.id, 'followed_id': john.id},
                {'follower_id': john.id, 'followed_id': jane.id},
                {'follower_id': jane.id, 'followed_id': twittor.id},
            ])

