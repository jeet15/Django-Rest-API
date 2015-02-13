from models import Player

from rest_framework import serializers

'''
class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name' , 'game', 'address')
'''

class PlayerSerializer(serializers.Serializer):
    name = serializers.CharField(label = 'Player Name')
    game = serializers.CharField(label = 'Game')
    address = serializers.CharField(label = 'Address')
    

    def create(self, data):
        """
        Create and return a new `Player` .
        """
        return Player.objects.create(**data)

    def update(self, player, data):

        """
        Update and return an existing `Player` 
        """
        player.name = data.get('name', player.name)
        player.game = data.get('game', player.game)
        player.address = data.get('address', player.address)
        player.save()
        return player