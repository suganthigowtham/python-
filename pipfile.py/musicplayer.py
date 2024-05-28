// TypeScript code
class Audio {
    constructor(public name: string, public url: string, public rating: number = 0) {}
}

class Playlist {
    audios: Audio[] = [];

    constructor(public name: string, public genre: string, public ratings: number[] = []) {}

    addAudio(audio: Audio) {
        this.audios.push(audio);
    }

    calculateAverageRating(): number {
        if (this.ratings.length === 0) return 0;
        const sum = this.ratings.reduce((total, rating) => total + rating, 0);
        return sum / this.ratings.length;
    }
}

class MusicPlayer {
    playlists: Playlist[] = [];

    createPlaylist(name: string, genre: string) {
        this.playlists.push(new Playlist(name, genre));
    }

    searchAudioByName(keyword: string): Audio[] {
        const results: Audio[] = [];
        for (const playlist of this.playlists) {
            for (const audio of playlist.audios) {
                if (audio.name.toLowerCase().includes(keyword.toLowerCase())) {
                    results.push(audio);
                }
            }
        }
        return results;
    }

    searchPlaylistByName(keyword: string): Playlist[] {
        return this.playlists.filter(playlist => playlist.name.toLowerCase().includes(keyword.toLowerCase()));
    }
}

// Sample usage
const player = new MusicPlayer();

// Create sample audios
const audio1 = new Audio("Song 1", "https://example.com/song1.mp3");
const audio2 = new Audio("Song 2", "https://example.com/song2.mp3");
const audio3 = new Audio("Song 3", "https://example.com/song3.mp3");

// Create sample playlists
player.createPlaylist("Playlist 1", "Rock");
player.playlists[0].addAudio(audio1);
player.playlists[0].addAudio(audio2);

player.createPlaylist("Playlist 2", "Pop");
player.playlists[1].addAudio(audio3);

// Search for audio by name
const searchResults = player.searchAudioByName("song");
console.log("Search Results:", searchResults);

// Search for playlist by name
const playlistResults = player.searchPlaylistByName("playlist");
console.log("Playlist Results:", playlistResults);

// Randomly generate ratings
const users = 3;
for (const playlist of player.playlists) {
    for (let i = 0; i < users; i++) {
        playlist.ratings.push(Math.floor(Math.random() * 5) + 1);
    }
    console.log(`Average rating for ${playlist.name}:`, playlist.calculateAverageRating());
}
n
