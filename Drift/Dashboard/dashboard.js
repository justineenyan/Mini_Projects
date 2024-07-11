const Recent = [
    {
        Name: 'Folderable Mini Drone.pdf',
        size:'8 MB',
        date:'2024-04-17'
    },
    {
        Name: 'LARVENDER KF102 Drone.pdf',
        size:'3 MB',
        date:'2024-04-17',
        
    },
    {
        Name: 'Ruko.png',
        size:'4 MB',
        date:'2024-04-17',
        
    },
    {
        Name: 'Camera.mp4',
        size:'12 MB',
        date:'2024-04-17',
    },
    {
        Name: 'GPS 4k Drone.pdf',
        size:'907 KB',
        date:'2024-04-17',
    },
    {
        Name: 'DJI.doc',
        size:'834 KB',
        date:'2024-04-17',
        
    },
    {
        Name: 'Lozenge.jpeg',
        size:'4 MB',
        date:'2024-04-17'
    }
]
if (document.getElementById('recent-files-table') != null){
    Recent.forEach(recent => {
        const tr = document.createElement('tr');
        const trContent = `
                        <td>${recent.Name}</td>
                        <td>${recent.size}</td>
                        <td>${recent.date}</td>
                        <td>
                            <a href="#"><i class="material-icons">file_download</i></a>
                            <a href="#"><i class="material-icons">delete</i></a>
                            <a href="#"><i class="material-icons">share</i></a>
                        </td>
                        `;
        tr.innerHTML = trContent;
        document.getElementById('recent-files-table').appendChild(tr);
    });
}

const Files = [
    {
      Name: 'Folderable Mini Drone.pdf',
      size: '8 MB',
      date: '2024-04-17'
    },
    {
      Name: 'Lozenge.jpeg',
      size: '4 MB',
      date: '2024-04-17'
    },
    {
      Name: 'Holiday pictures.zip',
      size: '25 MB',
      date: '2024-04-20'
    },
    {
      Name: 'Music playlist.txt',
      size: '2 KB',
      date: '2024-04-25'
    },
    {
      Name: 'Presentation.pptx',
      size: '15 MB',
      date: '2024-04-23'
    },
    {
      Name: 'Shopping list.txt',
      size: '1 KB',
      date: '2024-04-26'
    },
    {
      Name: 'Funny cat video.mp4',
      size: '50 MB',
      date: '2024-04-22'
    },
    {
      Name: 'Budget report.xlsx',
      size: '2 MB',
      date: '2024-04-24'
    },
    {
      Name: 'Birthday invitation.jpg',
      size: '750 KB',
      date: '2024-04-18'
    },
  ];
  
if (document.getElementById('files-table') != null){
    Files.forEach(file => {
        const tr = document.createElement('tr');
        const trContent = `
                        <td>${file.Name}</td>
                        <td>${file.size}</td>
                        <td>${file.date}</td>
                        <td>
                            <a href="#"><i class="material-icons">more_vert</i></a>
                        </td>
                        `;
        tr.innerHTML = trContent;
        document.getElementById('files-table').appendChild(tr);
    });
}