from application import db
from orator.orm import belongs_to, has_many, belongs_to_many
from message.models import Message

class User(db.Model):

    __fillable__ = ['name', 'email']

    __hidden__ = ['pivot']

    @has_many
    def messages(self):

        return Message

    @belongs_to_many(
        'followers',
        'followed_id', 'follower_id',
        with_timestamps=True
    )
    def followers(self):
        return User

    @belongs_to_many(
        'followers',
        'follower_id', 'followed_id',
        with_timestamps=True
    )
    def followed(self):
        return User

    def is_following(self, user):
        return self.followed().where('followed_id', user.id).exists()

    def is_followed_by(self, user):
        return self.followers().where('follower_id', user.id).exists()

    def follow(self, user):
        if not self.is_following(user):
            self.followed().attach(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed().detach(user)
