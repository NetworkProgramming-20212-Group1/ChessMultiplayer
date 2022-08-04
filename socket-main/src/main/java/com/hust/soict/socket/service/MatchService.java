package com.hust.soict.socket.service;

import com.hust.soict.socket.data_access.MatchRepo;
import com.hust.soict.socket.domain.Matches;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class MatchService {
    private final MatchRepo matchRepo;

    public MatchService(MatchRepo matchRepo) {
        this.matchRepo = matchRepo;
    }

    public Matches saveMatch(Matches matches) {
        Matches savedMatch = matchRepo.saveAndFlush(matches);
        return savedMatch;
    }

    public List<Matches> getMatches(String currentIngame) {
        return matchRepo.findByWhiteOrBlack(currentIngame, currentIngame);
    }
}
